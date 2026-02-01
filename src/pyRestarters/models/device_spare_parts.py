from enum import Enum


class DeviceSpareParts(str, Enum):
    MANUFACTURER = "Manufacturer"
    NO = "No"
    THIRD_PARTY = "Third party"

    def __str__(self) -> str:
        return str(self.value)
