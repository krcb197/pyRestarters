from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Category")


@_attrs_define
class Category:
    """A class of items.

    Attributes:
        id (Any | Unset): Unique identifier of this category Example: 1.
        name (Any | Unset): Unique name of this category Example: Scotland.
        powered (Any | Unset): Whether the item is powered (true) or unpowered (false) Example: true.
    """

    id: Any | Unset = UNSET
    name: Any | Unset = UNSET
    powered: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        powered = self.powered

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if powered is not UNSET:
            field_dict["powered"] = powered

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        powered = d.pop("powered", UNSET)

        category = cls(
            id=id,
            name=name,
            powered=powered,
        )

        category.additional_properties = d
        return category

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
