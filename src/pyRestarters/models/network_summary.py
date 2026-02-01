from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkSummary")


@_attrs_define
class NetworkSummary:
    """The summary information about a network.  For the full information, fetch the network.

    Attributes:
        id (Any): Unique identifier of this network Example: 1.
        summary (Any): Indicates that this is a summary result, not full network information. Example: true.
        name (Any | Unset): Unique name of this network Example: Default Network.
        logo (Any | Unset): URL of a logo for this network.  You should prefix this with /uploads before use. Example:
            /mid_1597853610178a4b76e4d666b2a7b32ee75d8a24c706f1cbf213970.png.
    """

    id: Any
    summary: Any
    name: Any | Unset = UNSET
    logo: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        summary = self.summary

        name = self.name

        logo = self.logo

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "summary": summary,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        summary = d.pop("summary")

        name = d.pop("name", UNSET)

        logo = d.pop("logo", UNSET)

        network_summary = cls(
            id=id,
            summary=summary,
            name=name,
            logo=logo,
        )

        network_summary.additional_properties = d
        return network_summary

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
