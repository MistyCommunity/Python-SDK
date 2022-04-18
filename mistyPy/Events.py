import json
import threading
import websocket

try:
    import thread
except ImportError:
    import _thread as thread
from random import randint


class Events:

    available_events = [
        'ActuatorPosition', 'ArTagDetection', 'AudioPlayComplete',
        'BatteryCharge', 'BumpSensor', 'CriticalStatusMessage', 'DialogAction',
        'DriveEncoders', 'FaceRecognition', 'FaceTraining', 'HaltCommand',
        'HazardNotification', 'IMU', 'KeyPhraseRecognized',
        'LocomotionCommand', 'ObjectDetection', 'ObstacleMap', 'PRUMessage',
        'RfCommMessage', 'RfCommState', 'RobotCommandMessage',
        'RobotInteractionState', 'SelfState', 'SerialMessage', 'SkillData',
        'SkillSystemStateChange', 'SourceFocusConfigMessage',
        'SourceTrackDataMessage', 'TextToSpeechComplete', 'TimeOfFlight',
        'TouchSensor', 'UserSkillData', 'VoiceRecord', 'WorldState'
    ]

    ActuatorPosition = 'ActuatorPosition'
    ArTagDetection = 'ArTagDetection'
    AudioPlayComplete = 'AudioPlayComplete'
    BatteryCharge = 'BatteryCharge'
    BumpSensor = 'BumpSensor'
    CriticalStatusMessage = 'CriticalStatusMessage'
    DialogAction = 'DialogAction'
    DriveEncoders = 'DriveEncoders'
    FaceRecognition = 'FaceRecognition'
    FaceTraining = 'FaceTraining'
    HaltCommand = 'HaltCommand'
    HazardNotification = 'HazardNotification'
    IMU = 'IMU'
    KeyPhraseRecognized = 'KeyPhraseRecognized'
    LocomotionCommand = 'LocomotionCommand'
    ObjectDetection = 'ObjectDetection'
    ObstacleMap = 'ObstacleMap'
    PRUMessage = 'PRUMessage'
    RfCommMessage = 'RfCommMessage'
    RfCommState = 'RfCommState'
    RobotCommandMessage = 'RobotCommandMessage'
    RobotInteractionState = 'RobotInteractionState'
    SelfState = 'SelfState'
    SerialMessage = 'SerialMessage'
    SkillData = 'SkillData'
    SkillSystemStateChange = 'SkillSystemStateChange'
    SourceFocusConfigMessage = 'SourceFocusConfigMessage'
    SourceTrackDataMessage = 'SourceTrackDataMessage'
    TextToSpeechComplete = 'TextToSpeechComplete'
    TimeOfFlight = 'TimeOfFlight'
    TouchSensor = 'TouchSensor'
    UserSkillData = 'UserSkillData'
    VoiceRecord = 'VoiceRecord'
    WorldState = 'WorldState'


class Event:
    def __init__(self,
                 ip,
                 event_type,
                 condition=None,
                 _debounce=0,
                 keep_alive=False,
                 callback_function=None):
        if event_type in Events.available_events:
            self.event_type = getattr(Events, event_type)
        else:
            self.is_active = False
            print(f"Invalid subscription:{event_type}")
            return
        self.ip = ip
        self.condition = condition
        self.debounce = _debounce
        self.data = json.loads(
            '{"status":"Not_Subscribed or just waiting for data"}')
        self.event_name = None
        self.ws = None
        self.initial_flag = True
        self.keep_alive = keep_alive
        self.callback_function = callback_function
        self.is_active = True

        self.thread = threading.Thread(target=self.initiate)
        self.thread.start()

    def initiate(self):
        websocket.enableTrace(
            False
        )  # Change this to true if you want to see all of the sent messages
        self.ws = websocket.WebSocketApp("ws://" + self.ip + "/pubsub",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)
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
