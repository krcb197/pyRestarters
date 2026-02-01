from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Alert")


@_attrs_define
class Alert:
    """An alert shown to users onsite.

    Attributes:
        id (Any): Unique identifier of this alert Example: 1.
        title (Any): The title of this alert Example: Support our work!.
        html (Any): HTML body of the alert
        start (Any): Start showing the alert at this time, in ISO8601 format. Example: 2022-09-18T11:30:00+00:00.
        end (Any): Stop showing the alert at this time, in ISO8601 format. Example: 2022-09-18T12:30:00+00:00.
        ctatitle (Any | Unset): (Optional) The text for a Call To Action button. Example: Double Your Donation Now.
        variant (Any | Unset): (Optional) The alert variant (default is secondary). Example: secondary.
        ctalink (Any | Unset): (Optional) The link for the button to direct to. Example:
            https://www.paypal.com/gb/fundraiser/charity/61071.
    """

    id: Any
    title: Any
    html: Any
    start: Any
    end: Any
    ctatitle: Any | Unset = UNSET
    variant: Any | Unset = UNSET
    ctalink: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        html = self.html

        start = self.start

        end = self.end

        ctatitle = self.ctatitle

        variant = self.variant

        ctalink = self.ctalink

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "title": title,
                "html": html,
                "start": start,
                "end": end,
            }
        )
        if ctatitle is not UNSET:
            field_dict["ctatitle"] = ctatitle
        if variant is not UNSET:
            field_dict["variant"] = variant
        if ctalink is not UNSET:
            field_dict["ctalink"] = ctalink

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        html = d.pop("html")

        start = d.pop("start")

        end = d.pop("end")

        ctatitle = d.pop("ctatitle", UNSET)

        variant = d.pop("variant", UNSET)

        ctalink = d.pop("ctalink", UNSET)

        alert = cls(
            id=id,
            title=title,
            html=html,
            start=start,
            end=end,
            ctatitle=ctatitle,
            variant=variant,
            ctalink=ctalink,
        )

        alert.additional_properties = d
        return alert

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
