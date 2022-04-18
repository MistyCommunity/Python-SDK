from requests import request, Response
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

    def get_audio_file(self,
                       fileName: str = None,
                       base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_audio_file"""

        json = {"fileName": fileName, "base64": base64}

        return self.get_request("audio", json=json)

    def get_camera_details(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_camera_details"""

        return self.get_request("camera")

    def get_video_recordings_list(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_video_recordings_list"""

        return self.get_request("videos/recordings/list")

    def get_log_level(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_log_level"""

        return self.get_request("logs/level")

    def get_websocket_version(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_websocket_version"""

        return self.get_request("websocket/version")

    def get_file(self, fileName: str = None, device: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_file"""

        json = {"fileName": fileName, "device": device}

        return self.get_request("files", json=json)

    def get_file_names(self,
                       directoryName: str = None,
                       device: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_file_names"""

        json = {"directoryName": directoryName, "device": device}

        return self.get_request("files/list", json=json)

    def get_loaded_contexts(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_loaded_contexts"""

        return self.get_request("dialogs/contexts")

    def get_action_commands(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_action_commands"""

        return self.get_request("actions/commands")

    def get_actions(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_actions"""

        return self.get_request("actions")

    def get_conversations(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_conversations"""

        return self.get_request("conversations")

    def get_states(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_states"""

        return self.get_request("states")

    def get_user_data(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_user_data"""

        return self.get_request("conversations/data")

    def updated_tutorials_check(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#updated_tutorials_check"""

        return self.get_request("tutorials/check")

    def get_video_recording(self,
                            name: str = None,
                            base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_video_recording"""

        json = {"name": name, "base64": base64}

        return self.get_request("videos/recordings", json=json)

    def get_available_wifi_networks(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_available_wifi_networks"""

        return self.get_request("networks/scan")

    def get_battery_level(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_battery_level"""

        return self.get_request("battery")

    def get_blink_settings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_blink_settings"""

        return self.get_request("blink/settings")

    def get_device_information(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_device_information"""

        return self.get_request("device")

    def get_hazard_settings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_hazard_settings"""

        return self.get_request("hazards/settings")

    def get_help(self, command: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_help"""

        json = {"command": command}

        return self.get_request("help", json=json)

    def get_image(self, fileName: str = None, base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_image"""

        json = {"fileName": fileName, "base64": base64}

        return self.get_request("images", json=json)

    def get_known_faces(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_known_faces"""

        return self.get_request("faces")

    def get_audio_list(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_audio_list"""

        return self.get_request("audio/list")

    def get_image_list(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_image_list"""

        return self.get_request("images/list")

    def get_video_list(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_video_list"""

        return self.get_request("videos/list")

    def get_log_file(self, date: datetime = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_log_file"""

        json = {"date": date}

        return self.get_request("logs", json=json)

    def get_manufacturing_mode_enabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_manufacturing_mode_enabled"""

        return self.get_request("manufacturing/enabled")

    def get_robot_update_settings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_robot_update_settings"""

        return self.get_request("system/update/settings")

    def get_running_skills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_running_skills"""

        return self.get_request("skills/running")

    def get_saved_wifi_networks(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_saved_wifi_networks"""

        return self.get_request("networks")

    def get_serial_sensor_values(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_serial_sensor_values"""

        return self.get_request("serial")

    def get_skills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_skills"""

        return self.get_request("skills")

    def get_store_update_available(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_store_update_available"""

        return self.get_request("system/updates")

    def get_video(self, fileName: str = None, base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_video"""

        json = {"fileName": fileName, "base64": base64}

        return self.get_request("videos", json=json)

    def get_volume(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_volume"""

        return self.get_request("audio/volume")

    def get_websocket_names(self, websocketClass: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_websocket_names"""

        json = {"websocketClass": websocketClass}

        return self.get_request("websockets", json=json)

    def audio_service_enabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#audio_service_enabled"""

        return self.get_request("services/audio")

    def get_av_streaming_service_enabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_av_streaming_service_enabled"""

        return self.get_request("services/avstreaming")

    def camera_service_enabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#camera_service_enabled"""

        return self.get_request("services/camera")

    def get_object_temperature(self,
                               roiLeft: int = None,
                               roiWidth: int = None,
                               roiTop: int = None,
                               roiHeight: int = None,
                               algorithm: int = None,
                               debug: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_object_temperature"""

        json = {
            "roiLeft": roiLeft,
            "roiWidth": roiWidth,
            "roiTop": roiTop,
            "roiHeight": roiHeight,
            "algorithm": algorithm,
            "debug": debug
        }

        return self.get_request("temperature/object", json=json)

    def get_subject_temperature(self,
                                calROILeft: int = None,
                                calROIWidth: int = None,
                                calROITop: int = None,
                                calROIHeight: int = None,
                                subjectROILeft: int = None,
                                subjectROIWidth: int = None,
                                subjectROITop: int = None,
                                subjectROIHeight: int = None,
                                calTemperature: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_subject_temperature"""

        json = {
            "calROILeft": calROILeft,
            "calROIWidth": calROIWidth,
            "calROITop": calROITop,
            "calROIHeight": calROIHeight,
            "subjectROILeft": subjectROILeft,
            "subjectROIWidth": subjectROIWidth,
            "subjectROITop": subjectROITop,
            "subjectROIHeight": subjectROIHeight,
            "calTemperature": calTemperature
        }

        return self.get_request("temperature/subject", json=json)

    def get_temperature_array(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_temperature_array"""

        return self.get_request("temperature/array")

    def take_picture(self,
                     base64: bool = None,
                     fileName: str = None,
                     width: int = None,
                     height: int = None,
                     displayOnScreen: bool = None,
                     overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#take_picture"""

        json = {
            "base64": base64,
            "fileName": fileName,
            "width": width,
            "height": height,
            "displayOnScreen": displayOnScreen,
            "overwriteExisting": overwriteExisting
        }

        return self.get_request("cameras/rgb", json=json)

    def get_python_output(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#get_python_output"""

        return self.get_request("python/output")

    def python_is_running(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#python_is_running"""

        return self.get_request("python/running")

    def put_file(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#put_file"""

        return self.post_request("files")

    def bluetooth_sensor_disconnect(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetooth_sensor_disconnect"""

        return self.post_request("bluetooth/rfcomm/disconnect")

    def bluetooth_sensor_discover_and_connect(
            self,
            name: str = None,
            serviceRecord: str = None,
            messageSize: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetooth_sensor_discover_and_connect"""

        json = {
            "name": name,
            "serviceRecord": serviceRecord,
            "messageSize": messageSize
        }

        return self.post_request("bluetooth/rfcomm/discoverandconnect",
                                 json=json)

    def bluetooth_sensor_send_message(self, message: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetooth_sensor_send_message"""

        json = {"message": message}

        return self.post_request("bluetooth/rfcomm/sendmessage", json=json)

    def configure_dialog(self,
                         nlpService: str = None,
                         nlpServiceKey: str = None,
                         nlpServiceRegion: str = None,
                         nlpServiceEndpoint: str = None,
                         asrService: str = None,
                         asrServiceKey: str = None,
                         asrServiceRegion: str = None,
                         asrServiceEndpoint: str = None,
                         ttsService: str = None,
                         ttsServiceKey: str = None,
                         ttsServiceRegion: str = None,
                         ttsServiceEndpoint: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#configure_dialog"""

        json = {
            "nlpService": nlpService,
            "nlpServiceKey": nlpServiceKey,
            "nlpServiceRegion": nlpServiceRegion,
            "nlpServiceEndpoint": nlpServiceEndpoint,
            "asrService": asrService,
            "asrServiceKey": asrServiceKey,
            "asrServiceRegion": asrServiceRegion,
            "asrServiceEndpoint": asrServiceEndpoint,
            "ttsService": ttsService,
            "ttsServiceKey": ttsServiceKey,
            "ttsServiceRegion": ttsServiceRegion,
            "ttsServiceEndpoint": ttsServiceEndpoint
        }

        return self.post_request("dialogs/configure", json=json)

    def play_and_listen(self,
                        audioFile: str = None,
                        context: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#play_and_listen"""

        json = {"audioFile": audioFile, "context": context}

        return self.post_request("dialogs/audio", json=json)

    def restore_nlp_model(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#restore_nlp_model"""

        return self.post_request("dialogs/restore")

    def set_context(self,
                    context: str = None,
                    filteredIntents: str = None,
                    overlapContexts: bool = None,
                    retrain: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_context"""

        json = {
            "context": context,
            "filteredIntents": filteredIntents,
            "overlapContexts": overlapContexts,
            "retrain": retrain
        }

        return self.post_request("dialogs/contexts", json=json)

    def speak_and_listen(self,
                         text: str = None,
                         flush: bool = None,
                         utteranceId: str = None,
                         context: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#speak_and_listen"""

        json = {
            "text": text,
            "flush": flush,
            "utteranceId": utteranceId,
            "context": context
        }

        return self.post_request("dialogs/ask", json=json)

    def start_dialog(self, sessionId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_dialog"""

        json = {"sessionId": sessionId}

        return self.post_request("dialogs/start", json=json)

    def stop_dialog(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_dialog"""

        return self.post_request("dialogs/stop")

    def train_nlp_engine(self,
                         context: str = None,
                         intents: object = None,
                         save: bool = None,
                         overwrite: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#train_nlp_engine"""

        json = {
            "context": context,
            "intents": intents,
            "save": save,
            "overwrite": overwrite
        }

        return self.post_request("dialogs/train", json=json)

    def update_dialog_settings(self,
                               userLanguage: int = None,
                               silenceTimeoutMs: int = None,
                               maxSpeechLengthMs: int = None,
                               sendInterimEvents: bool = None,
                               pitch: float = None,
                               speechRate: float = None,
                               voice: str = None,
                               confidence: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#update_dialog_settings"""

        json = {
            "userLanguage": userLanguage,
            "silenceTimeoutMs": silenceTimeoutMs,
            "maxSpeechLengthMs": maxSpeechLengthMs,
            "sendInterimEvents": sendInterimEvents,
            "pitch": pitch,
            "speechRate": speechRate,
            "voice": voice,
            "confidence": confidence
        }

        return self.post_request("dialogs/settings", json=json)

    def create_action(self,
                      name: str = None,
                      script: str = None,
                      overwrite: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#create_action"""

        json = {"name": name, "script": script, "overwrite": overwrite}

        return self.post_request("actions", json=json)

    def create_conversation(self,
                            name: str = None,
                            startingState: str = None,
                            description: str = None,
                            useVisionData: bool = None,
                            overwrite: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#create_conversation"""

        json = {
            "name": name,
            "startingState": startingState,
            "description": description,
            "useVisionData": useVisionData,
            "overwrite": overwrite
        }

        return self.post_request("conversations", json=json)

    def create_state(self,
                     name: str = None,
                     speak: str = None,
                     followUp: str = None,
                     audio: str = None,
                     listen: bool = None,
                     contexts: str = None,
                     preSpeech: str = None,
                     startAction: str = None,
                     speakingAction: str = None,
                     listeningAction: str = None,
                     processingAction: str = None,
                     transitionAction: str = None,
                     noMatchAction: str = None,
                     noMatchSpeech: str = None,
                     noMatchAudio: str = None,
                     repeatMaxCount: int = None,
                     failoverState: str = None,
                     retrain: bool = None,
                     overwrite: bool = None,
                     reEntrySpeech: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#create_state"""

        json = {
            "name": name,
            "speak": speak,
            "followUp": followUp,
            "audio": audio,
            "listen": listen,
            "contexts": contexts,
            "preSpeech": preSpeech,
            "startAction": startAction,
            "speakingAction": speakingAction,
            "listeningAction": listeningAction,
            "processingAction": processingAction,
            "transitionAction": transitionAction,
            "noMatchAction": noMatchAction,
            "noMatchSpeech": noMatchSpeech,
            "noMatchAudio": noMatchAudio,
            "repeatMaxCount": repeatMaxCount,
            "failoverState": failoverState,
            "retrain": retrain,
            "overwrite": overwrite,
            "reEntrySpeech": reEntrySpeech
        }

        return self.post_request("states", json=json)

    def create_user_data(self,
                         group: str = None,
                         match: str = None,
                         replaceString: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#create_user_data"""

        json = {"group": group, "match": match, "replaceString": replaceString}

        return self.post_request("conversations/data", json=json)

    def map_state(self,
                  conversation: str = None,
                  state: str = None,
                  trigger: str = None,
                  triggerFilter: str = None,
                  nextState: str = None,
                  detail: str = None,
                  nextConversation: str = None,
                  reEntry: bool = None,
                  includeFollowUp: bool = None,
                  overwrite: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#map_state"""

        json = {
            "conversation": conversation,
            "state": state,
            "trigger": trigger,
            "triggerFilter": triggerFilter,
            "nextState": nextState,
            "detail": detail,
            "nextConversation": nextConversation,
            "reEntry": reEntry,
            "includeFollowUp": includeFollowUp,
            "overwrite": overwrite
        }

        return self.post_request("conversations/map", json=json)

    def start_action(self,
                     name: str = None,
                     useVisionData: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_action"""

        json = {"name": name, "useVisionData": useVisionData}

        return self.post_request("actions/start", json=json)

    def start_conversation(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_conversation"""

        json = {"name": name}

        return self.post_request("conversations/start", json=json)

    def start_robot_interaction_event(self,
                                      useVisionData: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_robot_interaction_event"""

        json = {"useVisionData": useVisionData}

        return self.post_request("robotinteraction/start", json=json)

    def start_state(self,
                    name: str = None,
                    useVisionData: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_state"""

        json = {"name": name, "useVisionData": useVisionData}

        return self.post_request("states/start", json=json)

    def stop_action(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_action"""

        return self.post_request("actions/stop")

    def stop_conversation(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_conversation"""

        return self.post_request("conversations/stop")

    def stop_robot_interaction_event(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_robot_interaction_event"""

        return self.post_request("robotinteraction/stop")

    def trigger_conversation_event(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#trigger_conversation_event"""

        json = {"name": name}

        return self.post_request("conversations/trigger", json=json)

    def update_conversation(self,
                            currentName: str = None,
                            newName: str = None,
                            startingState: str = None,
                            useVisionData: bool = None,
                            description: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#update_conversation"""

        json = {
            "currentName": currentName,
            "newName": newName,
            "startingState": startingState,
            "useVisionData": useVisionData,
            "description": description
        }

        return self.post_request("conversations/update", json=json)

    def update_tutorials(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#update_tutorials"""

        return self.post_request("tutorials/update")

    def write_serial(self, message: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#write_serial"""

        json = {"message": message}

        return self.post_request("serial", json=json)

    def set_flashlight(self, on: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_flashlight"""

        json = {"on": on}

        return self.post_request("flashlight", json=json)

    def speak(self,
              text: str = None,
              pitch: float = None,
              speechRate: float = None,
              voice: str = None,
              flush: bool = None,
              utteranceId: str = None,
              language: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#speak"""

        json = {
            "text": text,
            "pitch": pitch,
            "speechRate": speechRate,
            "voice": voice,
            "flush": flush,
            "utteranceId": utteranceId,
            "language": language
        }

        return self.post_request("tts/speak", json=json)

    def speak_azure(self,
                    text: str = None,
                    isSSML: bool = None,
                    utteranceId: str = None,
                    speechKey: str = None,
                    speechRegion: str = None,
                    voice: str = None,
                    language: str = None,
                    useCaching: bool = None,
                    trimSilence: bool = None,
                    trimSilenceAggressiveness: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#speak_azure"""

        json = {
            "text": text,
            "isSSML": isSSML,
            "utteranceId": utteranceId,
            "speechKey": speechKey,
            "speechRegion": speechRegion,
            "voice": voice,
            "language": language,
            "useCaching": useCaching,
            "trimSilence": trimSilence,
            "trimSilenceAggressiveness": trimSilenceAggressiveness
        }

        return self.post_request("tts/speakazure", json=json)

    def start_av_streaming(self,
                           url: str = None,
                           width: int = None,
                           height: int = None,
                           frameRate: int = None,
                           videoBitRate: int = None,
                           audioBitRate: int = None,
                           audioSampleRateHz: int = None,
                           userName: str = None,
                           password: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_av_streaming"""

        json = {
            "url": url,
            "width": width,
            "height": height,
            "frameRate": frameRate,
            "videoBitRate": videoBitRate,
            "audioBitRate": audioBitRate,
            "audioSampleRateHz": audioSampleRateHz,
            "userName": userName,
            "password": password
        }

        return self.post_request("avstreaming/start", json=json)

    def start_recording_video(self,
                              fileName: str = None,
                              mute: bool = None,
                              duration: int = None,
                              width: int = None,
                              height: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_recording_video"""

        json = {
            "fileName": fileName,
            "mute": mute,
            "duration": duration,
            "width": width,
            "height": height
        }

        return self.post_request("video/record/start", json=json)

    def start_video_streaming(self,
                              port: int = None,
                              rotation: int = None,
                              width: int = None,
                              height: int = None,
                              quality: int = None,
                              overlay: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_video_streaming"""

        json = {
            "port": port,
            "rotation": rotation,
            "width": width,
            "height": height,
            "quality": quality,
            "overlay": overlay
        }

        return self.post_request("videostreaming/start", json=json)

    def stop_av_streaming(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_av_streaming"""

        return self.post_request("avstreaming/stop")

    def stop_recording_video(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_recording_video"""

        return self.post_request("video/record/stop")

    def stop_speaking(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_speaking"""

        return self.post_request("tts/stop")

    def stop_speaking_azure(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_speaking_azure"""

        return self.post_request("tts/stopazure")

    def perform_system_update(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#perform_system_update"""

        return self.post_request("system/update")

    def display_text(self, text: str = None, layer: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#display_text"""

        json = {"text": text, "layer": layer}

        return self.post_request("text/display", json=json)

    def allow_robot_updates(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#allow_robot_updates"""

        return self.post_request("system/update/allow")

    def cancel_skill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#cancel_skill"""

        json = {"skill": skill}

        return self.post_request("skills/cancel", json=json)

    def clear_error_text(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#clear_error_text"""

        return self.post_request("text/clear")

    def connect_to_saved_wifi(self, networkId: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#connect_to_saved_wifi"""

        json = {"networkId": networkId}

        return self.post_request("networks", json=json)

    def connect_wi_fi(self,
                      networkName: str = None,
                      password: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#connect_wi_fi"""

        json = {"networkName": networkName, "password": password}

        return self.post_request("networks/create", json=json)

    def disable_audio_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disable_audio_service"""

        return self.post_request("services/audio/disable")

    def disable_av_streaming_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disable_av_streaming_service"""

        return self.post_request("services/avstreaming/disable")

    def disable_camera_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disable_camera_service"""

        return self.post_request("services/camera/disable")

    def enable_audio_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enable_audio_service"""

        return self.post_request("services/audio/enable")

    def enable_av_streaming_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enable_av_streaming_service"""

        return self.post_request("services/avstreaming/enable")

    def enable_camera_service(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enable_camera_service"""

        return self.post_request("services/camera/enable")

    def override_skill_start(self,
                             skill: str = None,
                             startRule: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#override_skill_start"""

        json = {"skill": skill, "startRule": startRule}

        return self.post_request("skills/override", json=json)

    def pause_skill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#pause_skill"""

        json = {"skill": skill}

        return self.post_request("skills/pause", json=json)

    def perform_targeted_update(self,
                                components: str = None,
                                overrideBatteryCheck: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#perform_targeted_update"""

        json = {
            "components": components,
            "overrideBatteryCheck": overrideBatteryCheck
        }

        return self.post_request("system/update/component", json=json)

    def prevent_robot_updates(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#prevent_robot_updates"""

        return self.post_request("system/update/prevent")

    def reload_skills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#reload_skills"""

        return self.post_request("skills/reload")

    def rename_video_recording(self,
                               oldName: str = None,
                               newName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#rename_video_recording"""

        json = {"oldName": oldName, "newName": newName}

        return self.post_request("video/rename", json=json)

    def restart_robot(self,
                      core: bool = None,
                      sensoryServices: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#restart_robot"""

        json = {"core": core, "sensoryServices": sensoryServices}

        return self.post_request("reboot", json=json)

    def resume_skill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#resume_skill"""

        json = {"skill": skill}

        return self.post_request("skills/resume", json=json)

    def run_skill(self, skill: str = None, method: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#run_skill"""

        json = {"skill": skill, "method": method}

        return self.post_request("skills/start", json=json)

    def save_audio(self,
                   fileName: str = None,
                   data: str = None,
                   immediatelyApply: bool = None,
                   overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#save_audio"""

        json = {
            "fileName": fileName,
            "data": data,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.post_request("audio", json=json)

    def save_image(self,
                   fileName: str = None,
                   data: str = None,
                   width: int = None,
                   height: int = None,
                   immediatelyApply: bool = None,
                   overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#save_image"""

        json = {
            "fileName": fileName,
            "data": data,
            "width": width,
            "height": height,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.post_request("images", json=json)

    def save_skill_files(self,
                         file: bytes = None,
                         overwriteExisting: bool = None,
                         uniqueId: str = None,
                         authToken: str = None,
                         type: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#save_skill_files"""

        json = {
            "file": file,
            "overwriteExisting": overwriteExisting,
            "uniqueId": uniqueId,
            "authToken": authToken,
            "type": type
        }

        return self.post_request("skills", json=json)

    def save_video(self,
                   fileName: str = None,
                   data: str = None,
                   immediatelyApply: bool = None,
                   overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#save_video"""

        json = {
            "fileName": fileName,
            "data": data,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.post_request("videos", json=json)

    def set_blinking(self, blink: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_blinking"""

        json = {"blink": blink}

        return self.post_request("blink", json=json)

    def set_blink_settings(self,
                           revertToDefault: bool = None,
                           closedEyeMinMs: int = None,
                           closedEyeMaxMs: int = None,
                           openEyeMinMs: int = None,
                           openEyeMaxMs: int = None,
                           blinkImages: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_blink_settings"""

        json = {
            "revertToDefault": revertToDefault,
            "closedEyeMinMs": closedEyeMinMs,
            "closedEyeMaxMs": closedEyeMaxMs,
            "openEyeMinMs": openEyeMinMs,
            "openEyeMaxMs": openEyeMaxMs,
            "blinkImages": blinkImages
        }

        return self.post_request("blink/settings", json=json)

    def set_default_volume(self, volume: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_default_volume"""

        json = {"volume": volume}

        return self.post_request("audio/volume", json=json)

    def set_display_settings(self, revertToDefault: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_display_settings"""

        json = {"revertToDefault": revertToDefault}

        return self.post_request("display/settings", json=json)

    def set_image_display_settings(self,
                                   layer: str = None,
                                   revertToDefault: bool = None,
                                   deleted: bool = None,
                                   visible: bool = None,
                                   opacity: float = None,
                                   width: int = None,
                                   height: int = None,
                                   stretch: str = None,
                                   rotation: int = None,
                                   horizontalAlignment: str = None,
                                   verticalAlignment: str = None,
                                   placeOnTop: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_image_display_settings"""

        json = {
            "layer": layer,
            "revertToDefault": revertToDefault,
            "deleted": deleted,
            "visible": visible,
            "opacity": opacity,
            "width": width,
            "height": height,
            "stretch": stretch,
            "rotation": rotation,
            "horizontalAlignment": horizontalAlignment,
            "verticalAlignment": verticalAlignment,
            "placeOnTop": placeOnTop
        }

        return self.post_request("images/settings", json=json)

    def set_log_level(self,
                      localLogLevel: str = None,
                      remoteLogLevel: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_log_level"""

        json = {
            "localLogLevel": localLogLevel,
            "remoteLogLevel": remoteLogLevel
        }

        return self.post_request("logs/level", json=json)

    def set_notification_settings(self,
                                  revertToDefault: bool = None,
                                  ledEnabled: bool = None,
                                  keyPhraseEnabled: bool = None,
                                  keyPhraseFile: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_notification_settings"""

        json = {
            "revertToDefault": revertToDefault,
            "ledEnabled": ledEnabled,
            "keyPhraseEnabled": keyPhraseEnabled,
            "keyPhraseFile": keyPhraseFile
        }

        return self.post_request("notification/settings", json=json)

    def set_text_display_settings(self,
                                  layer: str = None,
                                  revertToDefault: bool = None,
                                  deleted: bool = None,
                                  visible: bool = None,
                                  opacity: float = None,
                                  size: int = None,
                                  weight: int = None,
                                  wrap: bool = None,
                                  horizontalAlignment: str = None,
                                  verticalAlignment: str = None,
                                  style: str = None,
                                  red: bytes = None,
                                  green: bytes = None,
                                  blue: bytes = None,
                                  padLeft: int = None,
                                  padTop: int = None,
                                  padRight: int = None,
                                  padBottom: int = None,
                                  rotation: int = None,
                                  fontFamily: str = None,
                                  placeOnTop: bool = None,
                                  width: int = None,
                                  height: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_text_display_settings"""

        json = {
            "layer": layer,
            "revertToDefault": revertToDefault,
            "deleted": deleted,
            "visible": visible,
            "opacity": opacity,
            "size": size,
            "weight": weight,
            "wrap": wrap,
            "horizontalAlignment": horizontalAlignment,
            "verticalAlignment": verticalAlignment,
            "style": style,
            "red": red,
            "green": green,
            "blue": blue,
            "padLeft": padLeft,
            "padTop": padTop,
            "padRight": padRight,
            "padBottom": padBottom,
            "rotation": rotation,
            "fontFamily": fontFamily,
            "placeOnTop": placeOnTop,
            "width": width,
            "height": height
        }

        return self.post_request("text/settings", json=json)

    def set_video_display_settings(self,
                                   layer: str = None,
                                   revertToDefault: bool = None,
                                   deleted: bool = None,
                                   visible: bool = None,
                                   opacity: float = None,
                                   width: int = None,
                                   height: int = None,
                                   stretch: str = None,
                                   rotation: int = None,
                                   horizontalAlignment: str = None,
                                   verticalAlignment: str = None,
                                   repeat: bool = None,
                                   placeOnTop: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_video_display_settings"""

        json = {
            "layer": layer,
            "revertToDefault": revertToDefault,
            "deleted": deleted,
            "visible": visible,
            "opacity": opacity,
            "width": width,
            "height": height,
            "stretch": stretch,
            "rotation": rotation,
            "horizontalAlignment": horizontalAlignment,
            "verticalAlignment": verticalAlignment,
            "repeat": repeat,
            "placeOnTop": placeOnTop
        }

        return self.post_request("video/settings", json=json)

    def set_websocket_version(self, version: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_websocket_version"""

        json = {"version": version}

        return self.post_request("websocket/version", json=json)

    def set_web_view_display_settings(self,
                                      layer: str = None,
                                      revertToDefault: bool = None,
                                      deleted: bool = None,
                                      visible: bool = None,
                                      width: int = None,
                                      height: int = None,
                                      stretch: str = None,
                                      horizontalAlignment: str = None,
                                      verticalAlignment: str = None,
                                      placeOnTop: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#set_web_view_display_settings"""

        json = {
            "layer": layer,
            "revertToDefault": revertToDefault,
            "deleted": deleted,
            "visible": visible,
            "width": width,
            "height": height,
            "stretch": stretch,
            "horizontalAlignment": horizontalAlignment,
            "verticalAlignment": verticalAlignment,
            "placeOnTop": placeOnTop
        }

        return self.post_request("webviews/settings", json=json)

    def start_wifi_hotspot(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_wifi_hotspot"""

        return self.post_request("networks/hotspot/start")

    def stop_wifi_hotspot(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_wifi_hotspot"""

        return self.post_request("networks/hotspot/stop")

    def trigger_skill_event(self,
                            skill: str = None,
                            eventName: str = None,
                            payload: str = None,
                            source: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#trigger_skill_event"""

        json = {
            "skill": skill,
            "eventName": eventName,
            "payload": payload,
            "source": source
        }

        return self.post_request("skills/event", json=json)

    def update_hazard_settings(self,
                               revertToDefault: bool = None,
                               disableTimeOfFlights: bool = None,
                               disableBumpSensors: bool = None,
                               bumpSensorsEnabled: str = None,
                               timeOfFlightThresholds: str = None,
                               disableTiltThreshold: bool = None,
                               tiltThreshold: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#update_hazard_settings"""

        json = {
            "revertToDefault": revertToDefault,
            "disableTimeOfFlights": disableTimeOfFlights,
            "disableBumpSensors": disableBumpSensors,
            "bumpSensorsEnabled": bumpSensorsEnabled,
            "timeOfFlightThresholds": timeOfFlightThresholds,
            "disableTiltThreshold": disableTiltThreshold,
            "tiltThreshold": tiltThreshold
        }

        return self.post_request("hazard/updatebasesettings", json=json)

    def cancel_face_training(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#cancel_face_training"""

        return self.post_request("faces/training/cancel")

    def capture_speech(self,
                       overwriteExisting: bool = None,
                       silenceTimeout: int = None,
                       maxSpeechLength: int = None,
                       requireKeyPhrase: bool = None,
                       speechRecognitionGrammar: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capture_speech"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "requireKeyPhrase": requireKeyPhrase,
            "speechRecognitionGrammar": speechRecognitionGrammar
        }

        return self.post_request("audio/speech/capture", json=json)

    def capture_speech_azure(self,
                             overwriteExisting: bool = None,
                             silenceTimeout: int = None,
                             maxSpeechLength: int = None,
                             requireKeyPhrase: bool = None,
                             captureFile: bool = None,
                             speechRecognitionLanguage: str = None,
                             azureSpeechKey: str = None,
                             azureSpeechRegion: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capture_speech_azure"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "requireKeyPhrase": requireKeyPhrase,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "azureSpeechKey": azureSpeechKey,
            "azureSpeechRegion": azureSpeechRegion
        }

        return self.post_request("audio/speech/captureazure", json=json)

    def capture_speech_google(self,
                              overwriteExisting: bool = None,
                              silenceTimeout: int = None,
                              maxSpeechLength: int = None,
                              requireKeyPhrase: bool = None,
                              captureFile: bool = None,
                              speechRecognitionLanguage: str = None,
                              googleSpeechKey: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capture_speech_google"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "requireKeyPhrase": requireKeyPhrase,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "googleSpeechKey": googleSpeechKey
        }

        return self.post_request("audio/speech/capturegoogle", json=json)

    def display_image(self,
                      fileName: str = None,
                      alpha: float = None,
                      layer: str = None,
                      isURL: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#display_image"""

        json = {
            "fileName": fileName,
            "alpha": alpha,
            "layer": layer,
            "isURL": isURL
        }

        return self.post_request("images/display", json=json)

    def change_led(self,
                   red: bytes = None,
                   green: bytes = None,
                   blue: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#change_led"""

        json = {"red": red, "green": green, "blue": blue}

        return self.post_request("led", json=json)

    def display_video(self,
                      filename: str = None,
                      layer: str = None,
                      isURL: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#display_video"""

        json = {"filename": filename, "layer": layer, "isURL": isURL}

        return self.post_request("videos/display", json=json)

    def display_web_view(self, url: str = None, layer: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#display_web_view"""

        json = {"url": url, "layer": layer}

        return self.post_request("webviews/display", json=json)

    def drive(self,
              linearVelocity: float = None,
              angularVelocity: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive"""

        json = {
            "linearVelocity": linearVelocity,
            "angularVelocity": angularVelocity
        }

        return self.post_request("drive", json=json)

    def drive_arc(self,
                  heading: float = None,
                  radius: float = None,
                  timeMs: float = None,
                  reverse: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive_arc"""

        json = {
            "heading": heading,
            "radius": radius,
            "timeMs": timeMs,
            "reverse": reverse
        }

        return self.post_request("drive/arc", json=json)

    def drive_time(self,
                   linearVelocity: float = None,
                   angularVelocity: float = None,
                   timeMs: int = None,
                   degree: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive_time"""

        json = {
            "linearVelocity": linearVelocity,
            "angularVelocity": angularVelocity,
            "timeMs": timeMs,
            "degree": degree
        }

        return self.post_request("drive/time", json=json)

    def halt(self, motorMask: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#halt"""

        json = {"motorMask": motorMask}

        return self.post_request("halt", json=json)

    def drive_heading(self,
                      heading: float = None,
                      distance: float = None,
                      timeMs: float = None,
                      reverse: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive_heading"""

        json = {
            "heading": heading,
            "distance": distance,
            "timeMs": timeMs,
            "reverse": reverse
        }

        return self.post_request("drive/hdt", json=json)

    def drive_track(self,
                    leftTrackSpeed: float = None,
                    rightTrackSpeed: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive_track"""

        json = {
            "leftTrackSpeed": leftTrackSpeed,
            "rightTrackSpeed": rightTrackSpeed
        }

        return self.post_request("drive/track", json=json)

    def move_arm(self,
                 arm: str = None,
                 position: float = None,
                 velocity: float = None,
                 duration: float = None,
                 units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#move_arm"""

        json = {
            "arm": arm,
            "position": position,
            "velocity": velocity,
            "duration": duration,
            "units": units
        }

        return self.post_request("arms", json=json)

    def move_arms(self,
                  leftArmPosition: float = None,
                  rightArmPosition: float = None,
                  leftArmVelocity: float = None,
                  rightArmVelocity: float = None,
                  duration: float = None,
                  units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#move_arms"""

        json = {
            "leftArmPosition": leftArmPosition,
            "rightArmPosition": rightArmPosition,
            "leftArmVelocity": leftArmVelocity,
            "rightArmVelocity": rightArmVelocity,
            "duration": duration,
            "units": units
        }

        return self.post_request("arms/set", json=json)

    def move_head(self,
                  pitch: float = None,
                  roll: float = None,
                  yaw: float = None,
                  velocity: float = None,
                  duration: float = None,
                  units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#move_head"""

        json = {
            "pitch": pitch,
            "roll": roll,
            "yaw": yaw,
            "velocity": velocity,
            "duration": duration,
            "units": units
        }

        return self.post_request("head", json=json)

    def pause_audio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#pause_audio"""

        return self.post_request("audio/pause")

    def play_audio(self, fileName: str = None, volume: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#play_audio"""

        json = {"fileName": fileName, "volume": volume}

        return self.post_request("audio/play", json=json)

    def start_python(self, code: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_python"""

        json = {"code": code}

        return self.post_request("python/start", json=json)

    def stop_python(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_python"""

        return self.post_request("python/stop")

    def send_external_request(self,
                              method: str = None,
                              resource: str = None,
                              authorizationType: str = None,
                              token: str = None,
                              arguments: bytes = None,
                              save: bool = None,
                              apply: bool = None,
                              fileName: str = None,
                              contentType: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#send_external_request"""

        json = {
            "method": method,
            "resource": resource,
            "authorizationType": authorizationType,
            "token": token,
            "arguments": arguments,
            "save": save,
            "apply": apply,
            "fileName": fileName,
            "contentType": contentType
        }

        return self.post_request("request", json=json)

    def start_ar_tag_detector(self,
                              dictionary: int = None,
                              tagSizeMm: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_ar_tag_detector"""

        json = {"dictionary": dictionary, "tagSizeMm": tagSizeMm}

        return self.post_request("artags/detection/start", json=json)

    def start_cascade_classifier(self,
                                 classifierId: int = None,
                                 scaleFactor: float = None,
                                 minNeighbors: int = None,
                                 minSizeWidth: int = None,
                                 minSizeHeight: int = None,
                                 maxSizeWidth: int = None,
                                 maxSizeHeight: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_cascade_classifier"""

        json = {
            "classifierId": classifierId,
            "scaleFactor": scaleFactor,
            "minNeighbors": minNeighbors,
            "minSizeWidth": minSizeWidth,
            "minSizeHeight": minSizeHeight,
            "maxSizeWidth": maxSizeWidth,
            "maxSizeHeight": maxSizeHeight
        }

        return self.post_request("cascadeclassifier/start", json=json)

    def start_face_detection(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_face_detection"""

        return self.post_request("faces/detection/start")

    def start_face_recognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_face_recognition"""

        return self.post_request("faces/recognition/start")

    def start_face_training(self, faceId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_face_training"""

        json = {"faceId": faceId}

        return self.post_request("faces/training/start", json=json)

    def start_key_phrase_recognition(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            speechRecognitionGrammar: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_key_phrase_recognition"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "captureSpeech": captureSpeech,
            "speechRecognitionGrammar": speechRecognitionGrammar
        }

        return self.post_request("audio/keyphrase/start", json=json)

    def start_key_phrase_recognition_azure(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            captureFile: bool = None,
            speechRecognitionLanguage: str = None,
            azureSpeechKey: str = None,
            azureSpeechRegion: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_key_phrase_recognition_azure"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "captureSpeech": captureSpeech,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "azureSpeechKey": azureSpeechKey,
            "azureSpeechRegion": azureSpeechRegion
        }

        return self.post_request("audio/keyphrase/startazure", json=json)

    def start_key_phrase_recognition_google(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            captureFile: bool = None,
            speechRecognitionLanguage: str = None,
            googleSpeechKey: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_key_phrase_recognition_google"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "captureSpeech": captureSpeech,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "googleSpeechKey": googleSpeechKey
        }

        return self.post_request("audio/keyphrase/startgoogle", json=json)

    def start_object_detector(self,
                              minimumConfidence: float = None,
                              modelId: int = None,
                              maxTrackerHistory: int = None,
                              delegateType: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_object_detector"""

        json = {
            "minimumConfidence": minimumConfidence,
            "modelId": modelId,
            "maxTrackerHistory": maxTrackerHistory,
            "delegateType": delegateType
        }

        return self.post_request("objects/detection/start", json=json)

    def start_pose_estimation(self,
                              minimumConfidence: float = None,
                              modelId: int = None,
                              delegateType: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_pose_estimation"""

        json = {
            "minimumConfidence": minimumConfidence,
            "modelId": modelId,
            "delegateType": delegateType
        }

        return self.post_request("humanposes/estimation/start", json=json)

    def start_qr_tag_detector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_qr_tag_detector"""

        return self.post_request("qrtags/detection/start")

    def start_recording_audio(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_recording_audio"""

        json = {"fileName": fileName}

        return self.post_request("audio/record/start", json=json)

    def start_recording_audio_raw(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_recording_audio_raw"""

        json = {"fileName": fileName}

        return self.post_request("audio/raw/record/start", json=json)

    def start_thermal_camera(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#start_thermal_camera"""

        return self.post_request("cameras/thermal/start")

    def stop(self, hold: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop"""

        json = {"hold": hold}

        return self.post_request("drive/stop", json=json)

    def stop_ar_tag_detector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_ar_tag_detector"""

        return self.post_request("artags/detection/stop")

    def stop_audio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_audio"""

        return self.post_request("audio/stop")

    def stop_cascade_classifier(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_cascade_classifier"""

        return self.post_request("cascadeclassifier/stop")

    def stop_face_detection(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_face_detection"""

        return self.post_request("faces/detection/stop")

    def stop_face_recognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_face_recognition"""

        return self.post_request("faces/recognition/stop")

    def stop_key_phrase_recognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_key_phrase_recognition"""

        return self.post_request("audio/keyphrase/stop")

    def stop_object_detector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_object_detector"""

        return self.post_request("objects/detection/stop")

    def stop_pose_estimation(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_pose_estimation"""

        return self.post_request("humanposes/estimation/stop")

    def stop_qr_tag_detector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_qr_tag_detector"""

        return self.post_request("qrtags/detection/stop")

    def stop_recording_audio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_recording_audio"""

        return self.post_request("audio/record/stop")

    def stop_thermal_camera(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_thermal_camera"""

        return self.post_request("cameras/thermal/stop")

    def stop_video_streaming(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop_video_streaming"""

        return self.post_request("videostreaming/stop")

    def transition_led(self,
                       red: bytes = None,
                       green: bytes = None,
                       blue: bytes = None,
                       red2: bytes = None,
                       green2: bytes = None,
                       blue2: bytes = None,
                       transitionType: str = None,
                       timeMs: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#transition_led"""

        json = {
            "red": red,
            "green": green,
            "blue": blue,
            "red2": red2,
            "green2": green2,
            "blue2": blue2,
            "transitionType": transitionType,
            "timeMs": timeMs
        }

        return self.post_request("led/transition", json=json)

    def delete_nlp_context(self, context: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_nlp_context"""

        json = {"context": context}

        return self.delete_request("dialogs/contexts", json=json)

    def delete_action(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_action"""

        json = {"name": name}

        return self.delete_request("actions", json=json)

    def delete_conversation(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_conversation"""

        json = {"name": name}

        return self.delete_request("conversations", json=json)

    def delete_state(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_state"""

        json = {"name": name}

        return self.delete_request("states", json=json)

    def delete_user_data(self,
                         group: str = None,
                         match: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_user_data"""

        json = {"group": group, "match": match}

        return self.delete_request("conversations/data", json=json)

    def remove_map_state(self,
                         conversation: str = None,
                         state: str = None,
                         trigger: str = None,
                         triggerFilter: str = None,
                         detail: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#remove_map_state"""

        json = {
            "conversation": conversation,
            "state": state,
            "trigger": trigger,
            "triggerFilter": triggerFilter,
            "detail": detail
        }

        return self.delete_request("conversations/map", json=json)

    def delete_audio(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_audio"""

        json = {"fileName": fileName}

        return self.delete_request("audio", json=json)

    def delete_image(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_image"""

        json = {"fileName": fileName}

        return self.delete_request("images", json=json)

    def delete_skill(self,
                     skill: str = None,
                     authToken: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_skill"""

        json = {"skill": skill, "authToken": authToken}

        return self.delete_request("skills", json=json)

    def delete_video(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_video"""

        json = {"fileName": fileName}

        return self.delete_request("videos", json=json)

    def delete_video_recording(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#delete_video_recording"""

        json = {"name": name}

        return self.delete_request("videos/recordings", json=json)

    def forget_wifi(self, networkId: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#forget_wifi"""

        json = {"networkId": networkId}

        return self.delete_request("networks", json=json)

    def remove_blink_mappings(self, blinkImages: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#remove_blink_mappings"""

        json = {"blinkImages": blinkImages}

        return self.delete_request("blink/images", json=json)

    def forget_faces(self, faceId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#forget_faces"""

        json = {"faceId": faceId}

        return self.delete_request("faces", json=json)
