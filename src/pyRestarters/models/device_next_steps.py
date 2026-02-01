from enum import Enum


class DeviceNextSteps(str, Enum):
    DO_IT_YOURSELF = "Do it yourself"
    MORE_TIME_NEEDED = "More time needed"
    PROFESSIONAL_HELP = "Professional help"

    def __str__(self) -> str:
        return str(self.value)
