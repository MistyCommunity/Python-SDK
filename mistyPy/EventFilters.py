def event_filter(name: str, comparison_operator: str, comparison_value):
    """

    :param name: The name of the item to filter on
    :param comparison_operator: How to compare values to determine if it is a valid event to send, Expected values: "=", "!=", ">", "<", ">=", "<=", "empty", "exists"
    :param comparison_value: The value to compare against.
    :return: Dictionary form of event filter, accepted in a list for the Event condition parameter
    """
    return {"Property": name, "Inequality": comparison_operator, "Value": comparison_value}

class EventFilters(object):

    @staticmethod
    def event_filter(name: str, comparison_operator: str, comparison_value):
        """

        :param name: The name of the item to filter on
        :param comparison_operator: How to compare values to determine if it is a valid event to send, Expected values: "=", "!=", ">", "<", ">=", "<=", "empty", "exists"
        :param comparison_value: The value to compare against.
        :return: Dictionary form of event filter, accepted in a list for the Event condition parameter
        """
        return event_filter(name, comparison_operator, comparison_value)

    class ActuatorPosition(object):
        ArmLeft = event_filter("SensorId", "=", "ala")
        ArmRight = event_filter("SensorId", "=", "ara")
        HeadPitch = event_filter("SensorId", "=", "ahp")
        HeadRoll = event_filter("SensorId", "=", "ahr")
        HeadYaw = event_filter("SensorId", "=", "ahy")

    class BumpSensorPosition(object):
        BackLeft = event_filter("SensorId", "=", "brl")
        BackRight = event_filter("SensorId", "=", "brr")
        FrontLeft = event_filter("SensorId", "=", "bfl")
        FrontRight = event_filter("SensorId", "=", "bfr")

    class CapTouchPosition(object):
        Chin = event_filter("SensorPosition", "=", "Chin")
        Scruff = event_filter("SensorPosition", "=", "Scruff")
        Right = event_filter("SensorPosition", "=", "HeadRight")
        Left = event_filter("SensorPosition", "=", "HeadLeft")
        Back = event_filter("SensorPosition", "=", "HeadBack")
        Front = event_filter("SensorPosition", "=", "HeadFront")

    class TimeOfFlightDistance(object):
        @staticmethod
        def MinDistance(value):
            return event_filter("DistanceInMeters", ">=", value)

        @staticmethod
        def MaxDistance(value):
            return event_filter("DistanceInMeters", "<=", value)

    class TimeOfFlightPosition(object):
        FrontLeft = event_filter("SensorPosition", "=", "Left")
        FrontRight = event_filter("SensorPosition", "=", "Right")
        FrontCenter = event_filter("SensorPosition", "=", "Center")
        Back = event_filter("SensorPosition", "=", "Back")
        DownwardBackLeft = event_filter("SensorPosition", "=", "DownBackLeft")
        DownwardBackRight = event_filter("SensorPosition", "=", "DownBackRight")
        DownwardFrontLeft = event_filter("SensorPosition", "=", "DownFrontLeft")
        DownwardFrontRight = event_filter("SensorPosition", "=", "DownFrontRight")

    class TimeOfFlightStatus(object):
        @staticmethod
        def MinStatus(value):
            return event_filter("Status", ">=", value)

        @staticmethod
        def MaxStatus(value):
            return event_filter("Status", "<=", value)

        @staticmethod
        def StatusEqual(value):
            event_filter("Status", "=", value)
