from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.device_barrier import DeviceBarrier
from ..models.device_next_steps import DeviceNextSteps
from ..models.device_repair_status import DeviceRepairStatus
from ..models.device_spare_parts import DeviceSpareParts
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.image import Image


T = TypeVar("T", bound="Device")


@_attrs_define
class Device:
    """An item which was examined at an Event.

    Attributes:
        id (Any): Unique identifier of this item. Example: 1.
        category (Any): The category to which this item belongs. Example: 16.
        item_type (Any): The name of the item. Example: Blender.
        eventid (Any | Unset): The event to which this device belongs. Example: 1.
        eventtitle (Any | Unset): Title of the event.  Provided for convenience to avoid extra API calls. Example:
            Europe/London.
        groupid (Any | Unset): The group to which this device belongs. Example: 1.
        groupname (Any | Unset): Name of the group. Provided for convenience to avoid extra API calls. Example:
            Restarters HQ.
        created_at (Any | Unset): When this device was first added Example: 2022-09-18T11:30:00+00:00.
        updated_at (Any | Unset): When this device was last updated Example: 2022-09-18T11:30:00+00:00.
        category_creation (Any | Unset): The id of the category to which this item belonged at the time of creation (if
            different). Example: 16.
        brand (Any | Unset): The brand or manufacturer of this item. Example: ACME.
        model (Any | Unset): The specific model of this item. Example: Wunderblender 2000.
        age (Any | Unset): The age of this item in years.  0 means the age is not known. Example: 1.5.
        estimate (Any | Unset): The weight estimage for this item in kg. Example: 1.5.
        problem (Any | Unset): Description of the problem/solution. Example: The power switch was broken..
        short_problem (Any | Unset): Shortened version of the of the problem/solution field. Example: The power switch
            was broken..
        notes (Any | Unset): Notes - repair difficulties, owner's perception of problem etc Example: I didn't have the
            right kind of screwdriver to open it up..
        repair_status (DeviceRepairStatus | Unset): Whether the item was fixed, is repairable, or cannot be fixed.
            Example: Fixed.
        next_steps (DeviceNextSteps | Unset): Iff repair_status is 'repairable', what the next steps are. Example: More
            time needed.
        spare_parts (DeviceSpareParts | Unset): Iff repair_status is 'repairable', whether any spare parts are needed.
            Example: Manufacturer.
        barrier (DeviceBarrier | Unset): Iff repair_status is 'End of life',  the primary barrier to repair. Example:
            Spare parts too expensive.
        images (list[Image] | Unset): Any images associated with this devices
    """

    id: Any
    category: Any
    item_type: Any
    eventid: Any | Unset = UNSET
    eventtitle: Any | Unset = UNSET
    groupid: Any | Unset = UNSET
    groupname: Any | Unset = UNSET
    created_at: Any | Unset = UNSET
    updated_at: Any | Unset = UNSET
    category_creation: Any | Unset = UNSET
    brand: Any | Unset = UNSET
    model: Any | Unset = UNSET
    age: Any | Unset = UNSET
    estimate: Any | Unset = UNSET
    problem: Any | Unset = UNSET
    short_problem: Any | Unset = UNSET
    notes: Any | Unset = UNSET
    repair_status: DeviceRepairStatus | Unset = UNSET
    next_steps: DeviceNextSteps | Unset = UNSET
    spare_parts: DeviceSpareParts | Unset = UNSET
    barrier: DeviceBarrier | Unset = UNSET
    images: list[Image] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        category = self.category

        item_type = self.item_type

        eventid = self.eventid

        eventtitle = self.eventtitle

        groupid = self.groupid

        groupname = self.groupname

        created_at = self.created_at

        updated_at = self.updated_at

        category_creation = self.category_creation

        brand = self.brand

        model = self.model

        age = self.age

        estimate = self.estimate

        problem = self.problem

        short_problem = self.short_problem

        notes = self.notes

        repair_status: str | Unset = UNSET
        if not isinstance(self.repair_status, Unset):
            repair_status = self.repair_status.value

        next_steps: str | Unset = UNSET
        if not isinstance(self.next_steps, Unset):
            next_steps = self.next_steps.value

        spare_parts: str | Unset = UNSET
        if not isinstance(self.spare_parts, Unset):
            spare_parts = self.spare_parts.value

        barrier: str | Unset = UNSET
        if not isinstance(self.barrier, Unset):
            barrier = self.barrier.value

        images: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.images, Unset):
            images = []
            for images_item_data in self.images:
                images_item = images_item_data.to_dict()
                images.append(images_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "category": category,
                "item_type": item_type,
            }
        )
        if eventid is not UNSET:
            field_dict["eventid"] = eventid
        if eventtitle is not UNSET:
            field_dict["eventtitle"] = eventtitle
        if groupid is not UNSET:
            field_dict["groupid"] = groupid
        if groupname is not UNSET:
            field_dict["groupname"] = groupname
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if category_creation is not UNSET:
            field_dict["category_creation"] = category_creation
        if brand is not UNSET:
            field_dict["brand"] = brand
        if model is not UNSET:
            field_dict["model"] = model
        if age is not UNSET:
            field_dict["age"] = age
        if estimate is not UNSET:
            field_dict["estimate"] = estimate
        if problem is not UNSET:
            field_dict["problem"] = problem
        if short_problem is not UNSET:
            field_dict["shortProblem"] = short_problem
        if notes is not UNSET:
            field_dict["notes"] = notes
        if repair_status is not UNSET:
            field_dict["repair_status"] = repair_status
        if next_steps is not UNSET:
            field_dict["next_steps"] = next_steps
        if spare_parts is not UNSET:
            field_dict["spare_parts"] = spare_parts
        if barrier is not UNSET:
            field_dict["barrier"] = barrier
        if images is not UNSET:
            field_dict["images"] = images

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.image import Image

        d = dict(src_dict)
        id = d.pop("id")

        category = d.pop("category")

        item_type = d.pop("item_type")

        eventid = d.pop("eventid", UNSET)

        eventtitle = d.pop("eventtitle", UNSET)

        groupid = d.pop("groupid", UNSET)

        groupname = d.pop("groupname", UNSET)

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        category_creation = d.pop("category_creation", UNSET)

        brand = d.pop("brand", UNSET)

        model = d.pop("model", UNSET)

        age = d.pop("age", UNSET)

        estimate = d.pop("estimate", UNSET)

        problem = d.pop("problem", UNSET)

        short_problem = d.pop("shortProblem", UNSET)

        notes = d.pop("notes", UNSET)

        _repair_status = d.pop("repair_status", UNSET)
        repair_status: DeviceRepairStatus | Unset
        if isinstance(_repair_status, Unset):
            repair_status = UNSET
        else:
            repair_status = DeviceRepairStatus(_repair_status)

        _next_steps = d.pop("next_steps", UNSET)
        next_steps: DeviceNextSteps | Unset
        if isinstance(_next_steps, Unset):
            next_steps = UNSET
        else:
            next_steps = DeviceNextSteps(_next_steps)

        _spare_parts = d.pop("spare_parts", UNSET)
        spare_parts: DeviceSpareParts | Unset
        if isinstance(_spare_parts, Unset):
            spare_parts = UNSET
        else:
            spare_parts = DeviceSpareParts(_spare_parts)

        _barrier = d.pop("barrier", UNSET)
        barrier: DeviceBarrier | Unset
        if isinstance(_barrier, Unset):
            barrier = UNSET
        else:
            barrier = DeviceBarrier(_barrier)

        _images = d.pop("images", UNSET)
        images: list[Image] | Unset = UNSET
        if _images is not UNSET:
            images = []
            for images_item_data in _images:
                images_item = Image.from_dict(images_item_data)

                images.append(images_item)

        device = cls(
            id=id,
            category=category,
            item_type=item_type,
            eventid=eventid,
            eventtitle=eventtitle,
            groupid=groupid,
            groupname=groupname,
            created_at=created_at,
            updated_at=updated_at,
            category_creation=category_creation,
            brand=brand,
            model=model,
            age=age,
            estimate=estimate,
            problem=problem,
            short_problem=short_problem,
            notes=notes,
            repair_status=repair_status,
            next_steps=next_steps,
            spare_parts=spare_parts,
            barrier=barrier,
            images=images,
        )

        device.additional_properties = d
        return device

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
