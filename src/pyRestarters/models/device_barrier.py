from enum import Enum


class DeviceBarrier(str, Enum):
    LACK_OF_EQUIPMENT = "Lack of equipment"
    NO_WAY_TO_OPEN_THE_PRODUCT = "No way to open the product"
    REPAIR_INFORMATION_NOT_AVAILABLE = "Repair information not available"
    SPARE_PARTS_NOT_AVAILABLE = "Spare parts not available"
    SPARE_PARTS_TOO_EXPENSIVE = "Spare parts too expensive"

    def __str__(self) -> str:
        return str(self.value)
