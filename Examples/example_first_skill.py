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


def start_skill():
    misty.RegisterEvent("initTTSComplete", Events.TextToSpeechComplete, keep_alive=False, callback_function=tts_intro_completed)

    misty.DisplayImage("e_defaultcontent.jpg")
    misty.MoveHead(0, 0, 0, 85)
    misty.Speak("I'd like to show you an image and have you tell me what you see.", None, None, None, True, "tts-content")

def tts_intro_completed(event):
    misty.DisplayImage("inkblot.jpg")
    # keep_alive defaults to false
    misty.RegisterEvent("whatDoYouSeeTTSComplete", Events.TextToSpeechComplete, callback_function=tts_what_do_you_see_completed)
    misty.Speak("What do you see when you look at this image?", None, None, None, True, "tts-content")

def tts_what_do_you_see_completed(event):
    misty.RegisterEvent("VoiceRecord", Events.VoiceRecord, callback_function=voice_record_complete)
    misty.CaptureSpeechAzure(True, 2000, 15000, False, False, "en-us", "<azure_cognitive_services_key>", "eastus")

def voice_record_complete(event):
    if "message" in event:
        parsed_message = event["message"]
        misty_heard = parsed_message["speechRecognitionResult"]
        print(f"Misty heard: {misty_heard}")
    # do something with this data
    misty.DisplayImage("e_defaultcontent.jpg")
    misty.MoveHead(-30, 20, -50, 85, None, None)
    misty.RegisterEvent("finalTTSComplete", Events.TextToSpeechComplete, callback_function=tts_all_i_ever_see)
    misty.Speak("That's interesting. All I ever see is a butterfly.", None, None, None, True, "tts-content")

def tts_all_i_ever_see(self, event):
    misty.DisplayImage("e_joy.jpg")


if __name__ == "__main__":
    ipAddress = "192.168.1.12"
    misty = Robot(ipAddress)
    start_skill()
