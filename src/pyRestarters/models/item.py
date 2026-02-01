from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Item")


@_attrs_define
class Item:
    """An item which can be specified in a Device

    Attributes:
        type_ (Any | Unset): The name of the item Example: Laptop.
        powered (Any | Unset): Whether the item is powered (true) or unpowered (false) Example: true.
        idcategories (Any | Unset): The id of the category for this item Example: 16.
        categoryname (Any | Unset): The name of the category for this item Example: Laptop medium.
    """

    type_: Any | Unset = UNSET
    powered: Any | Unset = UNSET
    idcategories: Any | Unset = UNSET
    categoryname: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        powered = self.powered

        idcategories = self.idcategories

        categoryname = self.categoryname

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if powered is not UNSET:
            field_dict["powered"] = powered
        if idcategories is not UNSET:
            field_dict["idcategories"] = idcategories
        if categoryname is not UNSET:
            field_dict["categoryname"] = categoryname

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = d.pop("type", UNSET)

        powered = d.pop("powered", UNSET)

        idcategories = d.pop("idcategories", UNSET)

        categoryname = d.pop("categoryname", UNSET)

        item = cls(
            type_=type_,
            powered=powered,
            idcategories=idcategories,
            categoryname=categoryname,
        )

        item.additional_properties = d
        return item

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
