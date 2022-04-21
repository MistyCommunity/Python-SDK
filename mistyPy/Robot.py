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

from .RobotCommands import RobotCommands
from .Events import Event
from time import sleep
from requests import exceptions

class Robot(RobotCommands):
    def __init__(self, ip='127.0.0.1'):
        self.ip = ip
        self.active_event_registrations = {}

    def register_event(self, event_type, event_name="", condition=None, debounce=0, keep_alive=False, callback_function=None):

        if callback_function is not None and callback_function.__code__.co_argcount != 1:
            print("Callback function must have one argument.")
            return

        if event_name is None or event_name == "":
            print(f"No event_name provided when registering to {event_type} - using default name {event_type}")
            event_name = event_type

        self.__remove_closed_events()

        if event_name in self.active_event_registrations:
            print(f"A registration already exists for event name {event_name}, ignoring request to register again")
            return

        new_registration = Event(self.ip, event_type, condition, debounce, keep_alive, callback_function)

        self.active_event_registrations[event_name] = new_registration

        return new_registration

    def unregister_event(self, event_name):
        if not event_name in self.active_event_registrations:
            print(f"Not currently registered to event: {event_name}")
            return
        
        try:
            self.active_event_registrations[event_name].unsubscribe()
        except:
            pass
        del self.active_event_registrations[event_name]

    def unregister_all_events(self):
        initial_event_names = list(self.active_event_registrations.keys())
        for event_name in initial_event_names:
            self.unregister_event(event_name)

    def get_registered_events(self):
        self.__remove_closed_events()
        return self.active_event_registrations.keys()

    def keep_alive(self):
        while True and len(self.active_event_registrations) > 0:
            self.__remove_closed_events()
            sleep(1)

    def __remove_closed_events(self):
        events_to_remove = []

        for event_name, event_subscription in self.active_event_registrations.items():
            if not event_subscription.is_active:
                events_to_remove.append(event_name)

        for event_name in events_to_remove:
            print(f"Event connection has closed for event: {event_name}")
            self.unregister_event(event_name)
