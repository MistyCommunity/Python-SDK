from requests import request, Response
from datetime import datetime
from collections import namedtuple

GridCell = namedtuple('GridCell', ['x', 'y'])


class RobotCommands:
    def __init__(self, ip: str = "127.0.0.1"):
        self.ip = ip

    def _genericRequest(self, verb: str, endpoint: str, **kwargs):
        url = "http://" + self.ip + "/api/" + endpoint
        return request(verb, url, **kwargs)

    def GetRequest(self, endpoint: str, **kwargs):
        return self._genericRequest("get", endpoint, **kwargs)

    def PostRequest(self, endpoint: str, **kwargs):
        return self._genericRequest("post", endpoint, **kwargs)

    def DeleteRequest(self, endpoint: str, **kwargs):
        return self._genericRequest("delete", endpoint, **kwargs)

    def PutRequest(self, endpoint: str, **kwargs):
        return self._genericRequest("put", endpoint, **kwargs)


#####################################################
#
#   All methods below this line were automatically
#   generated from the GenerateRobot.py class
#
#####################################################

    def GetAudioFile(self,
                     fileName: str = None,
                     base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getaudiofile"""

        json = {"fileName": fileName, "base64": base64}

        return self.GetRequest("audio", json=json)

    def GetCameraDetails(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getcameradetails"""

        return self.GetRequest("camera")

    def GetVideoRecordingsList(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getvideorecordingslist"""

        return self.GetRequest("videos/recordings/list")

    def GetLogLevel(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getloglevel"""

        return self.GetRequest("logs/level")

    def GetWebsocketVersion(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getwebsocketversion"""

        return self.GetRequest("websocket/version")

    def GetSlamMaps(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslammaps"""

        return self.GetRequest("slam/map/ids")

    def GetSlamNavigationDiagnostics(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslamnavigationdiagnostics"""

        return self.GetRequest("slam/diagnostics")

    def GetFile(self, fileName: str = None, device: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getfile"""

        json = {"fileName": fileName, "device": device}

        return self.GetRequest("files", json=json)

    def GetFileNames(self,
                     directoryName: str = None,
                     device: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getfilenames"""

        json = {"directoryName": directoryName, "device": device}

        return self.GetRequest("files/list", json=json)

    def TakeDepthPicture(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#takedepthpicture"""

        return self.GetRequest("cameras/depth")

    def TakeFisheyePicture(self, base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#takefisheyepicture"""

        json = {"base64": base64}

        return self.GetRequest("cameras/fisheye", json=json)

    def GetVideoRecording(self,
                          name: str = None,
                          base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getvideorecording"""

        json = {"name": name, "base64": base64}

        return self.GetRequest("videos/recordings", json=json)

    def AudioServiceEnabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#audioserviceenabled"""

        return self.GetRequest("services/audio")

    def GetAvStreamingServiceEnabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getavstreamingserviceenabled"""

        return self.GetRequest("services/avstreaming")

    def CameraServiceEnabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#cameraserviceenabled"""

        return self.GetRequest("services/camera")

    def SlamServiceEnabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#slamserviceenabled"""

        return self.GetRequest("services/slam")

    def GetCurrentSlamMap(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getcurrentslammap"""

        return self.GetRequest("slam/map/current")

    def GetSlamIrExposureAndGain(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslamirexposureandgain"""

        return self.GetRequest("slam/settings/ir")

    def GetSlamVisibleExposureAndGain(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslamvisibleexposureandgain"""

        return self.GetRequest("slam/settings/visible")

    def GetAvailableWifiNetworks(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getavailablewifinetworks"""

        return self.GetRequest("networks/scan")

    def GetBatteryLevel(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getbatterylevel"""

        return self.GetRequest("battery")

    def GetBlinkSettings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getblinksettings"""

        return self.GetRequest("blink/settings")

    def GetDeviceInformation(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getdeviceinformation"""

        return self.GetRequest("device")

    def GetHazardSettings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#gethazardsettings"""

        return self.GetRequest("hazards/settings")

    def GetHelp(self, command: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#gethelp"""

        json = {"command": command}

        return self.GetRequest("help", json=json)

    def GetImage(self, fileName: str = None, base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getimage"""

        json = {"fileName": fileName, "base64": base64}

        return self.GetRequest("images", json=json)

    def GetKnownFaces(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getknownfaces"""

        return self.GetRequest("faces")

    def GetAudioList(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getaudiolist"""

        return self.GetRequest("audio/list")

    def GetImageList(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getimagelist"""

        return self.GetRequest("images/list")

    def GetVideoList(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getvideolist"""

        return self.GetRequest("videos/list")

    def GetLogFile(self, date: datetime = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getlogfile"""

        json = {"date": date}

        return self.GetRequest("logs", json=json)

    def GetManufacturingModeEnabled(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getmanufacturingmodeenabled"""

        return self.GetRequest("manufacturing/enabled")

    def GetRobotUpdateSettings(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getrobotupdatesettings"""

        return self.GetRequest("system/update/settings")

    def GetRunningSkills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getrunningskills"""

        return self.GetRequest("skills/running")

    def GetSavedWifiNetworks(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getsavedwifinetworks"""

        return self.GetRequest("networks")

    def GetSerialSensorValues(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getserialsensorvalues"""

        return self.GetRequest("serial")

    def GetSkills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getskills"""

        return self.GetRequest("skills")

    def GetStoreUpdateAvailable(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getstoreupdateavailable"""

        return self.GetRequest("system/updates")

    def GetVideo(self, fileName: str = None, base64: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getvideo"""

        json = {"fileName": fileName, "base64": base64}

        return self.GetRequest("videos", json=json)

    def GetVolume(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getvolume"""

        return self.GetRequest("audio/volume")

    def GetWebsocketNames(self, websocketClass: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getwebsocketnames"""

        json = {"websocketClass": websocketClass}

        return self.GetRequest("websockets", json=json)

    def GetMap(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getmap"""

        return self.GetRequest("slam/map")

    def GetSlamPath(self,
                    x: int = None,
                    y: int = None,
                    minGap: float = None,
                    wallCostDistance: float = None,
                    unknownIsOpen: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslampath"""

        json = {
            "x": x,
            "y": y,
            "minGap": minGap,
            "wallCostDistance": wallCostDistance,
            "unknownIsOpen": unknownIsOpen
        }

        return self.GetRequest("slam/path", json=json)

    def GetSlamStatus(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#getslamstatus"""

        return self.GetRequest("slam/status")

    def TakePicture(self,
                    base64: bool = None,
                    fileName: str = None,
                    width: int = None,
                    height: int = None,
                    displayOnScreen: bool = None,
                    overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#takepicture"""

        json = {
            "base64": base64,
            "fileName": fileName,
            "width": width,
            "height": height,
            "displayOnScreen": displayOnScreen,
            "overwriteExisting": overwriteExisting
        }

        return self.GetRequest("cameras/rgb", json=json)

    def PutFile(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#putfile"""

        return self.PostRequest("files")

    def BluetoothSensorDisconnect(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetoothsensordisconnect"""

        return self.PostRequest("bluetooth/rfcomm/disconnect")

    def BluetoothSensorDiscoverAndConnect(
            self,
            name: str = None,
            serviceRecord: str = None,
            messageSize: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetoothsensordiscoverandconnect"""

        json = {
            "name": name,
            "serviceRecord": serviceRecord,
            "messageSize": messageSize
        }

        return self.PostRequest("bluetooth/rfcomm/discoverandconnect",
                                json=json)

    def BluetoothSensorSendMessage(self, message: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#bluetoothsensorsendmessage"""

        json = {"message": message}

        return self.PostRequest("bluetooth/rfcomm/sendmessage", json=json)

    def WriteSerial(self, message: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#writeserial"""

        json = {"message": message}

        return self.PostRequest("serial", json=json)

    def SetFlashlight(self, on: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setflashlight"""

        json = {"on": on}

        return self.PostRequest("flashlight", json=json)

    def Speak(self,
              text: str = None,
              pitch: float = None,
              speechRate: float = None,
              voice: str = None,
              flush: bool = None,
              utteranceId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#speak"""

        json = {
            "text": text,
            "pitch": pitch,
            "speechRate": speechRate,
            "voice": voice,
            "flush": flush,
            "utteranceId": utteranceId
        }

        return self.PostRequest("tts/speak", json=json)

    def SpeakAzure(self,
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
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#speakazure"""

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

        return self.PostRequest("tts/speakazure", json=json)

    def StartAvStreaming(self,
                         url: str = None,
                         width: int = None,
                         height: int = None,
                         frameRate: int = None,
                         videoBitRate: int = None,
                         audioBitRate: int = None,
                         audioSampleRateHz: int = None,
                         userName: str = None,
                         password: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startavstreaming"""

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

        return self.PostRequest("avstreaming/start", json=json)

    def StartRecordingVideo(self,
                            fileName: str = None,
                            mute: bool = None,
                            duration: int = None,
                            width: int = None,
                            height: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startrecordingvideo"""

        json = {
            "fileName": fileName,
            "mute": mute,
            "duration": duration,
            "width": width,
            "height": height
        }

        return self.PostRequest("video/record/start", json=json)

    def StopAvStreaming(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopavstreaming"""

        return self.PostRequest("avstreaming/stop")

    def StopRecordingVideo(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stoprecordingvideo"""

        return self.PostRequest("video/record/stop")

    def StopSpeaking(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopspeaking"""

        return self.PostRequest("tts/stop")

    def StopSpeakingAzure(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopspeakingazure"""

        return self.PostRequest("tts/stopazure")

    def StopSlamStreaming(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopslamstreaming"""

        return self.PostRequest("slam/streaming/stop")

    def DisplayText(self, text: str = None, layer: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#displaytext"""

        json = {"text": text, "layer": layer}

        return self.PostRequest("text/display", json=json)

    def ResetSlam(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#resetslam"""

        return self.PostRequest("slam/reset")

    def AllowRobotUpdates(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#allowrobotupdates"""

        return self.PostRequest("system/update/allow")

    def CancelSkill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#cancelskill"""

        json = {"skill": skill}

        return self.PostRequest("skills/cancel", json=json)

    def ClearErrorText(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#clearerrortext"""

        return self.PostRequest("text/clear")

    def ConnectToSavedWifi(self, networkId: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#connecttosavedwifi"""

        json = {"networkId": networkId}

        return self.PostRequest("networks", json=json)

    def ConnectWiFi(self,
                    networkName: str = None,
                    password: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#connectwifi"""

        json = {"networkName": networkName, "password": password}

        return self.PostRequest("networks/create", json=json)

    def DisableAudioService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disableaudioservice"""

        return self.PostRequest("services/audio/disable")

    def DisableAvStreamingService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disableavstreamingservice"""

        return self.PostRequest("services/avstreaming/disable")

    def DisableCameraService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disablecameraservice"""

        return self.PostRequest("services/camera/disable")

    def DisableSlamService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#disableslamservice"""

        return self.PostRequest("services/slam/disable")

    def EnableAudioService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enableaudioservice"""

        return self.PostRequest("services/audio/enable")

    def EnableAvStreamingService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enableavstreamingservice"""

        return self.PostRequest("services/avstreaming/enable")

    def EnableCameraService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enablecameraservice"""

        return self.PostRequest("services/camera/enable")

    def EnableSlamService(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#enableslamservice"""

        return self.PostRequest("services/slam/enable")

    def PauseSkill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#pauseskill"""

        json = {"skill": skill}

        return self.PostRequest("skills/pause", json=json)

    def PerformTargetedUpdate(self,
                              components: str = None,
                              overrideBatteryCheck: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#performtargetedupdate"""

        json = {
            "components": components,
            "overrideBatteryCheck": overrideBatteryCheck
        }

        return self.PostRequest("system/update/component", json=json)

    def PreventRobotUpdates(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#preventrobotupdates"""

        return self.PostRequest("system/update/prevent")

    def ReloadSkills(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#reloadskills"""

        return self.PostRequest("skills/reload")

    def RenameVideoRecording(self,
                             oldName: str = None,
                             newName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#renamevideorecording"""

        json = {"oldName": oldName, "newName": newName}

        return self.PostRequest("video/rename", json=json)

    def RestartRobot(self,
                     core: bool = None,
                     sensoryServices: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#restartrobot"""

        json = {"core": core, "sensoryServices": sensoryServices}

        return self.PostRequest("reboot", json=json)

    def ResumeSkill(self, skill: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#resumeskill"""

        json = {"skill": skill}

        return self.PostRequest("skills/resume", json=json)

    def RunSkill(self, skill: str = None, method: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#runskill"""

        json = {"skill": skill, "method": method}

        return self.PostRequest("skills/start", json=json)

    def SaveAudio(self,
                  fileName: str = None,
                  data: str = None,
                  immediatelyApply: bool = None,
                  overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#saveaudio"""

        json = {
            "fileName": fileName,
            "data": data,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.PostRequest("audio", json=json)

    def SaveImage(self,
                  fileName: str = None,
                  data: str = None,
                  width: int = None,
                  height: int = None,
                  immediatelyApply: bool = None,
                  overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#saveimage"""

        json = {
            "fileName": fileName,
            "data": data,
            "width": width,
            "height": height,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.PostRequest("images", json=json)

    def SaveSkillFiles(self,
                       file: bytes = None,
                       overwriteExisting: bool = None,
                       uniqueId: str = None,
                       authToken: str = None,
                       type: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#saveskillfiles"""

        json = {
            "file": file,
            "overwriteExisting": overwriteExisting,
            "uniqueId": uniqueId,
            "authToken": authToken,
            "type": type
        }

        return self.PostRequest("skills", json=json)

    def SaveVideo(self,
                  fileName: str = None,
                  data: str = None,
                  immediatelyApply: bool = None,
                  overwriteExisting: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#savevideo"""

        json = {
            "fileName": fileName,
            "data": data,
            "immediatelyApply": immediatelyApply,
            "overwriteExisting": overwriteExisting
        }

        return self.PostRequest("videos", json=json)

    def SetBlinking(self, blink: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setblinking"""

        json = {"blink": blink}

        return self.PostRequest("blink", json=json)

    def SetBlinkSettings(self,
                         revertToDefault: bool = None,
                         closedEyeMinMs: int = None,
                         closedEyeMaxMs: int = None,
                         openEyeMinMs: int = None,
                         openEyeMaxMs: int = None,
                         blinkImages: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setblinksettings"""

        json = {
            "revertToDefault": revertToDefault,
            "closedEyeMinMs": closedEyeMinMs,
            "closedEyeMaxMs": closedEyeMaxMs,
            "openEyeMinMs": openEyeMinMs,
            "openEyeMaxMs": openEyeMaxMs,
            "blinkImages": blinkImages
        }

        return self.PostRequest("blink/settings", json=json)

    def SetDefaultVolume(self, volume: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setdefaultvolume"""

        json = {"volume": volume}

        return self.PostRequest("audio/volume", json=json)

    def SetDisplaySettings(self, revertToDefault: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setdisplaysettings"""

        json = {"revertToDefault": revertToDefault}

        return self.PostRequest("display/settings", json=json)

    def SetImageDisplaySettings(self,
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
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setimagedisplaysettings"""

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

        return self.PostRequest("images/settings", json=json)

    def SetLogLevel(self,
                    localLogLevel: str = None,
                    remoteLogLevel: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setloglevel"""

        json = {
            "localLogLevel": localLogLevel,
            "remoteLogLevel": remoteLogLevel
        }

        return self.PostRequest("logs/level", json=json)

    def SetNotificationSettings(self,
                                revertToDefault: bool = None,
                                ledEnabled: bool = None,
                                keyPhraseEnabled: bool = None,
                                keyPhraseFile: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setnotificationsettings"""

        json = {
            "revertToDefault": revertToDefault,
            "ledEnabled": ledEnabled,
            "keyPhraseEnabled": keyPhraseEnabled,
            "keyPhraseFile": keyPhraseFile
        }

        return self.PostRequest("notification/settings", json=json)

    def SetTextDisplaySettings(self,
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
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#settextdisplaysettings"""

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

        return self.PostRequest("text/settings", json=json)

    def SetVideoDisplaySettings(self,
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
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setvideodisplaysettings"""

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

        return self.PostRequest("video/settings", json=json)

    def SetWebsocketVersion(self, version: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setwebsocketversion"""

        json = {"version": version}

        return self.PostRequest("websocket/version", json=json)

    def SetWebViewDisplaySettings(self,
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
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setwebviewdisplaysettings"""

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

        return self.PostRequest("webviews/settings", json=json)

    def StartWifiHotspot(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startwifihotspot"""

        return self.PostRequest("networks/hotspot/start")

    def StopWifiHotspot(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopwifihotspot"""

        return self.PostRequest("networks/hotspot/stop")

    def RenameSlamMap(self, key: str = None, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#renameslammap"""

        json = {"key": key, "name": name}

        return self.PostRequest("slam/map/rename", json=json)

    def SetCurrentSlamMap(self, key: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setcurrentslammap"""

        json = {"key": key}

        return self.PostRequest("slam/map/current", json=json)

    def SetSlamIrExposureAndGain(self,
                                 exposure: float = None,
                                 gain: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setslamirexposureandgain"""

        json = {"exposure": exposure, "gain": gain}

        return self.PostRequest("slam/settings/ir", json=json)

    def SetSlamVisibleExposureAndGain(self,
                                      exposure: float = None,
                                      gain: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#setslamvisibleexposureandgain"""

        json = {"exposure": exposure, "gain": gain}

        return self.PostRequest("slam/settings/visible", json=json)

    def TriggerSkillEvent(self,
                          skill: str = None,
                          eventName: str = None,
                          payload: str = None,
                          source: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#triggerskillevent"""

        json = {
            "skill": skill,
            "eventName": eventName,
            "payload": payload,
            "source": source
        }

        return self.PostRequest("skills/event", json=json)

    def UpdateHazardSettings(self,
                             revertToDefault: bool = None,
                             disableTimeOfFlights: bool = None,
                             disableBumpSensors: bool = None,
                             bumpSensorsEnabled: str = None,
                             timeOfFlightThresholds: str = None,
                             disableTiltThreshold: bool = None,
                             tiltThreshold: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#updatehazardsettings"""

        json = {
            "revertToDefault": revertToDefault,
            "disableTimeOfFlights": disableTimeOfFlights,
            "disableBumpSensors": disableBumpSensors,
            "bumpSensorsEnabled": bumpSensorsEnabled,
            "timeOfFlightThresholds": timeOfFlightThresholds,
            "disableTiltThreshold": disableTiltThreshold,
            "tiltThreshold": tiltThreshold
        }

        return self.PostRequest("hazard/updatebasesettings", json=json)

    def PerformSystemUpdate(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#performsystemupdate"""

        return self.PostRequest("system/update")

    def CancelFaceTraining(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#cancelfacetraining"""

        return self.PostRequest("faces/training/cancel")

    def CaptureSpeech(self,
                      overwriteExisting: bool = None,
                      silenceTimeout: int = None,
                      maxSpeechLength: int = None,
                      requireKeyPhrase: bool = None,
                      speechRecognitionGrammar: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capturespeech"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "requireKeyPhrase": requireKeyPhrase,
            "speechRecognitionGrammar": speechRecognitionGrammar
        }

        return self.PostRequest("audio/speech/capture", json=json)

    def CaptureSpeechAzure(self,
                           overwriteExisting: bool = None,
                           silenceTimeout: int = None,
                           maxSpeechLength: int = None,
                           requireKeyPhrase: bool = None,
                           captureFile: bool = None,
                           speechRecognitionLanguage: str = None,
                           azureSpeechKey: str = None,
                           azureSpeechRegion: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capturespeechazure"""

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

        return self.PostRequest("audio/speech/captureazure", json=json)

    def CaptureSpeechGoogle(self,
                            overwriteExisting: bool = None,
                            silenceTimeout: int = None,
                            maxSpeechLength: int = None,
                            requireKeyPhrase: bool = None,
                            captureFile: bool = None,
                            speechRecognitionLanguage: str = None,
                            googleSpeechKey: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#capturespeechgoogle"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "requireKeyPhrase": requireKeyPhrase,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "googleSpeechKey": googleSpeechKey
        }

        return self.PostRequest("audio/speech/capturegoogle", json=json)

    def DisplayImage(self,
                     fileName: str = None,
                     alpha: float = None,
                     layer: str = None,
                     isURL: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#displayimage"""

        json = {
            "fileName": fileName,
            "alpha": alpha,
            "layer": layer,
            "isURL": isURL
        }

        return self.PostRequest("images/display", json=json)

    def ChangeLED(self,
                  red: bytes = None,
                  green: bytes = None,
                  blue: bytes = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#changeled"""

        json = {"red": red, "green": green, "blue": blue}

        return self.PostRequest("led", json=json)

    def DisplayVideo(self,
                     filename: str = None,
                     layer: str = None,
                     isURL: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#displayvideo"""

        json = {"filename": filename, "layer": layer, "isURL": isURL}

        return self.PostRequest("videos/display", json=json)

    def DisplayWebView(self, url: str = None, layer: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#displaywebview"""

        json = {"url": url, "layer": layer}

        return self.PostRequest("webviews/display", json=json)

    def Drive(self,
              linearVelocity: float = None,
              angularVelocity: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drive"""

        json = {
            "linearVelocity": linearVelocity,
            "angularVelocity": angularVelocity
        }

        return self.PostRequest("drive", json=json)

    def DriveArc(self,
                 heading: float = None,
                 radius: float = None,
                 timeMs: float = None,
                 reverse: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drivearc"""

        json = {
            "heading": heading,
            "radius": radius,
            "timeMs": timeMs,
            "reverse": reverse
        }

        return self.PostRequest("drive/arc", json=json)

    def DriveTime(self,
                  linearVelocity: float = None,
                  angularVelocity: float = None,
                  timeMs: int = None,
                  degree: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drivetime"""

        json = {
            "linearVelocity": linearVelocity,
            "angularVelocity": angularVelocity,
            "timeMs": timeMs,
            "degree": degree
        }

        return self.PostRequest("drive/time", json=json)

    def DriveToLocation(self, destination: GridCell = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drivetolocation"""

        json = {"destination": destination}

        return self.PostRequest("drive/coordinates", json=json)

    def FollowPath(self,
                   path: str = None,
                   velocity: float = None,
                   fullSpinDuration: float = None,
                   waypointAccuracy: float = None,
                   rotateThreshold: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#followpath"""

        json = {
            "path": path,
            "velocity": velocity,
            "fullSpinDuration": fullSpinDuration,
            "waypointAccuracy": waypointAccuracy,
            "rotateThreshold": rotateThreshold
        }

        return self.PostRequest("drive/path", json=json)

    def Halt(self, motorMask: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#halt"""

        json = {"motorMask": motorMask}

        return self.PostRequest("halt", json=json)

    def DriveHeading(self,
                     heading: float = None,
                     distance: float = None,
                     timeMs: float = None,
                     reverse: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#driveheading"""

        json = {
            "heading": heading,
            "distance": distance,
            "timeMs": timeMs,
            "reverse": reverse
        }

        return self.PostRequest("drive/hdt", json=json)

    def DriveTrack(self,
                   leftTrackSpeed: float = None,
                   rightTrackSpeed: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#drivetrack"""

        json = {
            "leftTrackSpeed": leftTrackSpeed,
            "rightTrackSpeed": rightTrackSpeed
        }

        return self.PostRequest("drive/track", json=json)

    def MoveArm(self,
                arm: str = None,
                position: float = None,
                velocity: float = None,
                duration: float = None,
                units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#movearm"""

        json = {
            "arm": arm,
            "position": position,
            "velocity": velocity,
            "duration": duration,
            "units": units
        }

        return self.PostRequest("arms", json=json)

    def MoveArms(self,
                 leftArmPosition: float = None,
                 rightArmPosition: float = None,
                 leftArmVelocity: float = None,
                 rightArmVelocity: float = None,
                 duration: float = None,
                 units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#movearms"""

        json = {
            "leftArmPosition": leftArmPosition,
            "rightArmPosition": rightArmPosition,
            "leftArmVelocity": leftArmVelocity,
            "rightArmVelocity": rightArmVelocity,
            "duration": duration,
            "units": units
        }

        return self.PostRequest("arms/set", json=json)

    def MoveHead(self,
                 pitch: float = None,
                 roll: float = None,
                 yaw: float = None,
                 velocity: float = None,
                 duration: float = None,
                 units: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#movehead"""

        json = {
            "pitch": pitch,
            "roll": roll,
            "yaw": yaw,
            "velocity": velocity,
            "duration": duration,
            "units": units
        }

        return self.PostRequest("head", json=json)

    def PauseAudio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#pauseaudio"""

        return self.PostRequest("audio/pause")

    def PlayAudio(self, fileName: str = None, volume: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#playaudio"""

        json = {"fileName": fileName, "volume": volume}

        return self.PostRequest("audio/play", json=json)

    def SendExternalRequest(self,
                            method: str = None,
                            resource: str = None,
                            authorizationType: str = None,
                            token: str = None,
                            arguments: bytes = None,
                            save: bool = None,
                            apply: bool = None,
                            fileName: str = None,
                            contentType: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#sendexternalrequest"""

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

        return self.PostRequest("request", json=json)

    def StartArTagDetector(self,
                           dictionary: int = None,
                           tagSizeMm: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startartagdetector"""

        json = {"dictionary": dictionary, "tagSizeMm": tagSizeMm}

        return self.PostRequest("artags/detection/start", json=json)

    def StartCascadeClassifier(self,
                               classifierId: int = None,
                               scaleFactor: float = None,
                               minNeighbors: int = None,
                               minSizeWidth: int = None,
                               minSizeHeight: int = None,
                               maxSizeWidth: int = None,
                               maxSizeHeight: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startcascadeclassifier"""

        json = {
            "classifierId": classifierId,
            "scaleFactor": scaleFactor,
            "minNeighbors": minNeighbors,
            "minSizeWidth": minSizeWidth,
            "minSizeHeight": minSizeHeight,
            "maxSizeWidth": maxSizeWidth,
            "maxSizeHeight": maxSizeHeight
        }

        return self.PostRequest("cascadeclassifier/start", json=json)

    def StartFaceDetection(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startfacedetection"""

        return self.PostRequest("faces/detection/start")

    def StartFaceRecognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startfacerecognition"""

        return self.PostRequest("faces/recognition/start")

    def StartFaceTraining(self, faceId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startfacetraining"""

        json = {"faceId": faceId}

        return self.PostRequest("faces/training/start", json=json)

    def StartKeyPhraseRecognition(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            speechRecognitionGrammar: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startkeyphraserecognition"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "captureSpeech": captureSpeech,
            "speechRecognitionGrammar": speechRecognitionGrammar
        }

        return self.PostRequest("audio/keyphrase/start", json=json)

    def StartKeyPhraseRecognitionAzure(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            captureFile: bool = None,
            speechRecognitionLanguage: str = None,
            azureSpeechKey: str = None,
            azureSpeechRegion: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startkeyphraserecognitionazure"""

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

        return self.PostRequest("audio/keyphrase/startazure", json=json)

    def StartKeyPhraseRecognitionGoogle(
            self,
            overwriteExisting: bool = None,
            silenceTimeout: int = None,
            maxSpeechLength: int = None,
            captureSpeech: int = None,
            captureFile: bool = None,
            speechRecognitionLanguage: str = None,
            googleSpeechKey: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startkeyphraserecognitiongoogle"""

        json = {
            "overwriteExisting": overwriteExisting,
            "silenceTimeout": silenceTimeout,
            "maxSpeechLength": maxSpeechLength,
            "captureSpeech": captureSpeech,
            "captureFile": captureFile,
            "speechRecognitionLanguage": speechRecognitionLanguage,
            "googleSpeechKey": googleSpeechKey
        }

        return self.PostRequest("audio/keyphrase/startgoogle", json=json)

    def StartObjectDetector(self,
                            minimumConfidence: float = None,
                            modelId: int = None,
                            maxTrackerHistory: int = None,
                            delegateType: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startobjectdetector"""

        json = {
            "minimumConfidence": minimumConfidence,
            "modelId": modelId,
            "maxTrackerHistory": maxTrackerHistory,
            "delegateType": delegateType
        }

        return self.PostRequest("objects/detection/start", json=json)

    def StartPoseEstimation(self,
                            minimumConfidence: float = None,
                            modelId: int = None,
                            delegateType: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startposeestimation"""

        json = {
            "minimumConfidence": minimumConfidence,
            "modelId": modelId,
            "delegateType": delegateType
        }

        return self.PostRequest("humanposes/estimation/start", json=json)

    def StartQrTagDetector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startqrtagdetector"""

        return self.PostRequest("qrtags/detection/start")

    def StartRecordingAudio(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startrecordingaudio"""

        json = {"fileName": fileName}

        return self.PostRequest("audio/record/start", json=json)

    def StartRecordingAudioRaw(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startrecordingaudioraw"""

        json = {"fileName": fileName}

        return self.PostRequest("audio/raw/record/start", json=json)

    def Stop(self, hold: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stop"""

        json = {"hold": hold}

        return self.PostRequest("drive/stop", json=json)

    def StopArTagDetector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopartagdetector"""

        return self.PostRequest("artags/detection/stop")

    def StopAudio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopaudio"""

        return self.PostRequest("audio/stop")

    def StopCascadeClassifier(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopcascadeclassifier"""

        return self.PostRequest("cascadeclassifier/stop")

    def StopFaceDetection(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopfacedetection"""

        return self.PostRequest("faces/detection/stop")

    def StopFaceRecognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopfacerecognition"""

        return self.PostRequest("faces/recognition/stop")

    def StopKeyPhraseRecognition(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopkeyphraserecognition"""

        return self.PostRequest("audio/keyphrase/stop")

    def StopObjectDetector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopobjectdetector"""

        return self.PostRequest("objects/detection/stop")

    def StopPoseEstimation(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopposeestimation"""

        return self.PostRequest("humanposes/estimation/stop")

    def StopQrTagDetector(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopqrtagdetector"""

        return self.PostRequest("qrtags/detection/stop")

    def StopRecordingAudio(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stoprecordingaudio"""

        return self.PostRequest("audio/record/stop")

    def StartLocatingDockingStation(
            self,
            startStreamingTimeout: int = None,
            enableIrTimeout: int = None,
            enableAutoExposure: bool = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startlocatingdockingstation"""

        json = {
            "startStreamingTimeout": startStreamingTimeout,
            "enableIrTimeout": enableIrTimeout,
            "enableAutoExposure": enableAutoExposure
        }

        return self.PostRequest("slam/docking/start", json=json)

    def StartMapping(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startmapping"""

        return self.PostRequest("slam/map/start")

    def StartObstacleDetection(self, updateRate: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startobstacledetection"""

        json = {"updateRate": updateRate}

        return self.PostRequest("slam/obstacle/start", json=json)

    def StartSlamStreaming(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#startslamstreaming"""

        return self.PostRequest("slam/streaming/start")

    def StartTracking(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#starttracking"""

        return self.PostRequest("slam/track/start")

    def StopLocatingDockingStation(self,
                                   stopStreamingTimeout: int = None,
                                   disableIrTimeout: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stoplocatingdockingstation"""

        json = {
            "stopStreamingTimeout": stopStreamingTimeout,
            "disableIrTimeout": disableIrTimeout
        }

        return self.PostRequest("slam/docking/stop", json=json)

    def StopMapping(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopmapping"""

        return self.PostRequest("slam/map/stop")

    def StopObstacleDetection(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stopobstacledetection"""

        return self.PostRequest("slam/obstacle/stop")

    def StopTracking(self) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#stoptracking"""

        return self.PostRequest("slam/track/stop")

    def TransitionLED(self,
                      red: bytes = None,
                      green: bytes = None,
                      blue: bytes = None,
                      red2: bytes = None,
                      green2: bytes = None,
                      blue2: bytes = None,
                      transitionType: str = None,
                      timeMs: float = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#transitionled"""

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

        return self.PostRequest("led/transition", json=json)

    def DeleteAudio(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deleteaudio"""

        json = {"fileName": fileName}

        return self.DeleteRequest("audio", json=json)

    def DeleteImage(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deleteimage"""

        json = {"fileName": fileName}

        return self.DeleteRequest("images", json=json)

    def DeleteSkill(self,
                    skill: str = None,
                    authToken: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deleteskill"""

        json = {"skill": skill, "authToken": authToken}

        return self.DeleteRequest("skills", json=json)

    def DeleteVideo(self, fileName: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deletevideo"""

        json = {"fileName": fileName}

        return self.DeleteRequest("videos", json=json)

    def DeleteVideoRecording(self, name: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deletevideorecording"""

        json = {"name": name}

        return self.DeleteRequest("videos/recordings", json=json)

    def ForgetWifi(self, networkId: int = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#forgetwifi"""

        json = {"networkId": networkId}

        return self.DeleteRequest("networks", json=json)

    def RemoveBlinkMappings(self, blinkImages: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#removeblinkmappings"""

        json = {"blinkImages": blinkImages}

        return self.DeleteRequest("blink/images", json=json)

    def DeleteSlamMap(self, key: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#deleteslammap"""

        json = {"key": key}

        return self.DeleteRequest("slam/map", json=json)

    def ForgetFaces(self, faceId: str = None) -> Response:
        """https://docs.mistyrobotics.com/misty-ii/reference/rest/#forgetfaces"""

        json = {"faceId": faceId}

        return self.DeleteRequest("faces", json=json)
