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

# Add mistyPy directory to sys path
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from mistyPy.Robot import Robot
from mistyPy.Events import Events
from mistyPy.EventFilters import EventFilters
from time import time

ROBOT_IP = "192.168.1.45"

misty_robot = Robot(ROBOT_IP)

def log_tof_reading(message):
    tof_message = message["message"]

    print(f"{tof_message['created'][:-1].replace('T',' ')},{tof_message['sensorId']},{tof_message['distanceInMeters']},{tof_message['status']},{tof_message['inHazard']},{tof_message['signal']},{tof_message['sigma']}", file=f)
    f.flush()


if __name__ == "__main__":
    f = open(f"tof_logs_{time()}.csv", "w")
    print("time,sensor id,distance,status,in hazard,signal,sigma", file=f)

    try:
        # Subscribe to the tofs individually so each message from each tof is written to a new line
        front_right = misty_robot.register_event("frontright", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.FrontRight], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        front_center = misty_robot.register_event("frontcenter", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.FrontCenter], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        front_left = misty_robot.register_event("frontleft", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.FrontLeft], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        back_range = misty_robot.register_event("back", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.Back], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        down_front_right = misty_robot.register_event("downfrontright", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.DownwardFrontRight], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        down_front_left = misty_robot.register_event("downfrontleft", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.DownwardFrontLeft], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        down_back_right = misty_robot.register_event("downbackright", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.DownwardBackRight], keep_alive=True, callback_function=log_tof_reading, debounce=5)
        down_back_left = misty_robot.register_event("downbackleft", Events.TimeOfFlight, condition=[EventFilters.TimeOfFlightPosition.DownwardBackLeft], keep_alive=True, callback_function=log_tof_reading, debounce=5)

        # Use the keep_alive() function if you want to keep the main thread alive, otherwise the event threads will also get killed once processing has stopped
        misty_robot.keep_alive()

    except Exception as ex:
        print(ex)
    finally:
        f.close()
        # Unregister from all events or the spawned threads won't get killed
        misty_robot.unregister_all_events()
