"""/**********************************************************************
    Copyright 2021 Misty Robotics
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
        http://www.apache.org/licenses/LICENSE-2.0
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    **WARRANTY DISCLAIMER.**
    * General. TO THE MAXIMUM EXTENT PERMITTED BY APPLICABLE LAW, MISTY
    ROBOTICS PROVIDES THIS SAMPLE SOFTWARE "AS-IS" AND DISCLAIMS ALL
    WARRANTIES AND CONDITIONS, WHETHER EXPRESS, IMPLIED, OR STATUTORY,
    INCLUDING THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
    PURPOSE, TITLE, QUIET ENJOYMENT, ACCURACY, AND NON-INFRINGEMENT OF
    THIRD-PARTY RIGHTS. MISTY ROBOTICS DOES NOT GUARANTEE ANY SPECIFIC
    RESULTS FROM THE USE OF THIS SAMPLE SOFTWARE. MISTY ROBOTICS MAKES NO
    WARRANTY THAT THIS SAMPLE SOFTWARE WILL BE UNINTERRUPTED, FREE OF VIRUSES
    OR OTHER HARMFUL CODE, TIMELY, SECURE, OR ERROR-FREE.
    * Use at Your Own Risk. YOU USE THIS SAMPLE SOFTWARE AND THE PRODUCT AT
    YOUR OWN DISCRETION AND RISK. YOU WILL BE SOLELY RESPONSIBLE FOR (AND MISTY
    ROBOTICS DISCLAIMS) ANY AND ALL LOSS, LIABILITY, OR DAMAGES, INCLUDING TO
    ANY HOME, PERSONAL ITEMS, PRODUCT, OTHER PERIPHERALS CONNECTED TO THE PRODUCT,
    COMPUTER, AND MOBILE DEVICE, RESULTING FROM YOUR USE OF THIS SAMPLE SOFTWARE
    OR PRODUCT.
    Please refer to the Misty Robotics End User License Agreement for further
    information and full details:
        https://www.mistyrobotics.com/legal/end-user-license-agreement/
**********************************************************************/"""

from requests import request, exceptions
from os import linesep, path
from yapf.yapflib.yapf_api import FormatFile

class Argument:
    def __init__(self, name: str, value_type: object, nullable: bool, ordinal_number: int):
        self.name = name
        self.value_type = value_type
        self.nullable = nullable
        self.ordinal_number = ordinal_number

    def __str__(self):
        return str({"Name": self.name,
                    "Type": self.value_type,
                    "Nullable": self.nullable,
                    "ordinalNumber": self.ordinal_number})

    # To enable sorting arguments by ordinal number
    def __lt__(self, other):
        return self.ordinal_number < other.ordinal_number

class Command:
    def __init__(self, name: str, verb: str, endpoint: str, arguments: dict, command_group: str):
        self.name = name
        self.endpoint = endpoint
        self.verb = verb
        self.commandGroup = command_group
        self.arguments = self.parse_arguments(arguments)

    def __str__(self):
        arguments = []
        for argument in self.arguments:
            arguments.append(str(argument))

        return str({"Name": self.name,
                    "Endpoint": self.endpoint,
                    "Verb": self.verb,
                    "CommandGroup": self.commandGroup,
                    "Arguments": arguments})

    @staticmethod
    def parse_arguments(arguments: dict):
        # The current types that get passed from the help command to their python equivalents
        type_switch = {
            "String": "str",
            "Boolean": "bool",
            "DateTime": "datetime",
            "Int32": "int",
            "Double": "float",
            "Byte[]": "bytes",
            "Byte": "bytes",
            "Single": "float",
            "GridCell": "GridCell",
            "Object": "object"
        }

        parsed_args = []

        for argument in arguments:
            value_type = arguments[argument]["getValueType"]

            # The value type only comes in nullable or not nullable, examples of both:
            # Not nullable: "System.String, System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
            # Nullable: "System.Nullable`1[[System.Int32, System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a]], System.Private.CoreLib, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"
            nullable = True if value_type.find("System.Nullable") > -1 else False
            type_def = value_type.split(", ")[0].split(".")[-1]
            ordinal_number = arguments[argument]["ordinalNumber"]

            parsed_arg = Argument(argument, type_switch[type_def], nullable, ordinal_number)

            parsed_args.append(parsed_arg)

        return parsed_args

def pythonicate_name(name):
    for i in range(0, len(name)):
        if name[i].isupper():
            if i > 0:
                name = name[:i] + "_" + name[i].lower() + name[i + 1:]
                i += 2
            else:
                name = name[:i] + name[i].lower() + name[i + 1:]
                i += 1
            if i < len(name) and name[i].isupper():
                while i < len(name) and name[i].isupper():
                    name = name[:i] + name[i].lower() + name[i + 1:]
                    i += 1
                if i < len(name):
                    name = name[:i - 1] + "_" + name[i - 1:]
    return name

class RobotGenerator:
    def __init__(self, ip: str = "127.0.0.1"):
        self.ip = ip
        self.path = path.dirname(path.realpath(__file__))
        self.commands = self.generate_commands()
        self.events = self.generate_events()
        self.write_robot()
        self.write_events()

    def generate_commands(self):
        commands = []
        help_response = self.get_request("help").json()

        for verb in help_response["result"]:
            for command in help_response["result"][verb]:
                new_command = Command(pythonicate_name(command["apiCommand"]["name"]), verb, command["endpoint"],
                                      command["apiCommand"]["arguments"], command["apiCommand"]["apiCommandGroup"])

                commands.append(new_command)

        return commands

    def write_robot(self):
        with open(f"{self.path}/RobotCommands.py", "wt") as outfile:
            outfile.write("""from requests import request, Response
from datetime import datetime
from collections import namedtuple

GridCell = namedtuple('GridCell', ['x', 'y'])

class RobotCommands:
    def __init__(self, ip: str = "127.0.0.1"):
        self.ip = ip

    def _generic_request(self, verb: str, endpoint: str, **kwargs):
        url = "http://" + self.ip + "/api/" + endpoint
        return request(verb, url, **kwargs)

    def get_request(self, endpoint: str, **kwargs):
        return self._generic_request("get", endpoint, **kwargs)

    def post_request(self, endpoint: str, **kwargs):
        return self._generic_request("post", endpoint, **kwargs)

    def delete_request(self, endpoint: str, **kwargs):
        return self._generic_request("delete", endpoint, **kwargs)
    
    def put_request(self, endpoint: str, **kwargs):
        return self._generic_request("put", endpoint, **kwargs)

#####################################################
#
#   All methods below this line were automatically
#   generated from the GenerateRobot.py class
#
#####################################################

""")
            for command in self.commands:
                robot_method = self.parse_command_into_method(command)

                print(robot_method, file=outfile, end='')
                print("\n\n", file=outfile)

        FormatFile(f"{self.path}/RobotCommands.py", in_place=True)

    def parse_command_into_method(self, command: Command):
        """

        :type command: Command
        """
        verb_switch = {"get": "get_request",
                       "post": "post_request",
                       "delete": "delete_request",
                       "put": "put_request"}

        method_arguments = self.parse_arguments_into_kwargs(command.arguments)

        if len(command.arguments) > 0:
            method_string = f"    def {command.name}(self, {method_arguments}) -> Response:\n"
        else:
            method_string = f"    def {command.name}(self) -> Response:\n"

        method_string += f"        \"\"\"https://docs.mistyrobotics.com/misty-ii/reference/rest/#{command.name.lower()}\"\"\"\n"

        if len(command.arguments) > 0:
            method_string += f"\n        json = {{\n"
        for argument in command.arguments:
            method_string += f"            \"{argument.name}\" : {argument.name},\n"

        passed_args = ""
        if len(command.arguments) > 0:
            # -2 is the magic number to remove the trailing comma and newline character from the last argument
            method_string = method_string[:-2] + "\n        }\n"
            passed_args = "json=json"

        if passed_args == "":
            method_string += f"""
        return self.{verb_switch[command.verb]}(\"{command.endpoint}\")"""
        else:
            method_string += f"""
        return self.{verb_switch[command.verb]}(\"{command.endpoint}\", {passed_args})"""

        return method_string

    def parse_arguments_into_kwargs(self, arguments: list[Argument]):
        if len(arguments) == 0:
            return

        args_definition = ""

        for argument in sorted(arguments):
            if args_definition != "":
                args_definition += ", "
            args_definition += f"{argument.name} : {argument.value_type} = None"

        return args_definition

    def _generic_request(self, verb: str, endpoint: str, **kwargs):
        url = "http://" + self.ip + "/api/" + endpoint
        return request(verb, url, **kwargs)

    def get_request(self, endpoint: str, **kwargs):
        return self._generic_request("get", endpoint, **kwargs)

    def generate_events(self):
        event_response = self.get_request("websockets").json()

        event_names = [event["class"] for event in event_response["result"]]

        return sorted(event_names)

    def write_events(self):
        with open(f"{self.path}/Events.py", "wt") as outfile:
            outfile.write("""import json
import threading
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
from random import randint

class Events:

""")
            outfile.write(f"    available_events = {self.events}{linesep}")
            for event in self.events:
                outfile.write(f"    {event} = '{event}'\n")
            outfile.write("""class Event:

    def __init__(self, ip, event_type, condition=None, _debounce=0, keep_alive=False, callback_function=None):
        if event_type in Events.available_events:
            self.event_type = getattr(Events, event_type)
        else:
            self.is_active = False
            print(f"Invalid subscription:{event_type}")
            return
        self.ip = ip        
        self.condition = condition
        self.debounce = _debounce
        self.data = json.loads('{"status":"Not_Subscribed or just waiting for data"}')
        self.event_name = None
        self.ws = None
        self.initial_flag = True
        self.keep_alive = keep_alive
        self.callback_function = callback_function
        self.is_active = True

        self.thread = threading.Thread(target=self.initiate)
        self.thread.start()

    def initiate(self):
        websocket.enableTrace(False)  # Change this to true if you want to see all of the sent messages
        self.ws = websocket.WebSocketApp("ws://" + self.ip + "/pubsub", on_message=self.on_message,
                                         on_error=self.on_error, on_close=self.on_close, on_open=self.on_open)
        self.ws.run_forever(ping_timeout=10)

    def on_message(self, message):
        # The first message is the successful subscription message
        if self.initial_flag:
            self.initial_flag = False
        else:
            self.data = json.loads(message)

            if self.callback_function is not None:
                self.callback_function(self.data)
            if not self.keep_alive:
                self.unsubscribe()

    def on_error(self, error):
        print(error)

    def on_close(self):
        self.is_active = False

    def on_open(self):
        def run(*args):
            self.ws.send(str(self.get_subscribe_message()))

        thread.start_new_thread(run, ())
        self.is_active = True

    def unsubscribe(self):
        self.ws.send(str(self.get_unsubscribe_message()))
        self.ws.close()
        self.is_active = False

    def get_subscribe_message(self):
        self.event_name = str(randint(0, 10000000000))

        if self.condition is None:
            subscribe_msg = {
                "Operation": "subscribe",
                "Type": self.event_type,
                "DebounceMs": self.debounce,
                "EventName": self.event_name,
                "Message": ""
            }

        else:
            subscribe_msg = {
                "Operation": "subscribe",
                "Type": self.event_type,
                "DebounceMs": self.debounce,
                "EventName": self.event_name,
                "Message": "",
                "EventConditions": self.condition
            }

        return subscribe_msg

    def get_unsubscribe_message(self):
        unsubscribe_msg = {
            "Operation": "unsubscribe",
            "EventName": self.event_name,
            "Message": ""
        }

        return unsubscribe_msg
""")

        FormatFile(f"{self.path}/Events.py", in_place=True)
