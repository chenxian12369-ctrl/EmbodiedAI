from enum import Enum


class RobotState(Enum):

    SEARCHING = "searching"

    TRACKING = "tracking"

    STABLE = "stable"

    MOVING = "moving"

    FINISHED = "finished"

    ERROR = "error"