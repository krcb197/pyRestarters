from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Volunteer")


@_attrs_define
class Volunteer:
    """A volunteer on a group or event.

    Attributes:
        id (Any | Unset): Unique identifier of this record (i.e. the event/group and user combination) Example: 1.
        user (Any | Unset): Unique identifier of this volunteer's user record Example: 2.
        name (Any | Unset): The volunteer's name Example: Sam.
        host (Any | Unset): Whether the volunteer is a host of the event/group Example: false.
        image (Any | Unset): URL of an image for this user.  You should prefix this with /uploads before use. Example:
            /mid_1597853610178a4b76e4d666b2a7b32ee75d8a24c706f1cbf213970.png.
    """

    id: Any | Unset = UNSET
    user: Any | Unset = UNSET
    name: Any | Unset = UNSET
    host: Any | Unset = UNSET
    image: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        user = self.user

        name = self.name

        host = self.host

        image = self.image

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if user is not UNSET:
            field_dict["user"] = user
        if name is not UNSET:
            field_dict["name"] = name
        if host is not UNSET:
            field_dict["host"] = host
        if image is not UNSET:
            field_dict["image"] = image

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        user = d.pop("user", UNSET)

        name = d.pop("name", UNSET)

        host = d.pop("host", UNSET)

        image = d.pop("image", UNSET)

        volunteer = cls(
            id=id,
            user=user,
            name=name,
            host=host,
            image=image,
        )

        volunteer.additional_properties = d
        return volunteer

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
