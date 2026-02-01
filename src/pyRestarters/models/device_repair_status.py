from enum import Enum


class DeviceRepairStatus(str, Enum):
    END_OF_LIFE = "End of life"
    FIXED = "Fixed"
    REPAIRABLE = "Repairable"

    def __str__(self) -> str:
        return str(self.value)
