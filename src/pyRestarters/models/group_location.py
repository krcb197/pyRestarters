from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GroupLocation")


@_attrs_define
class GroupLocation:
    """The information about the location of a group.

    Attributes:
        area (Any | Unset): The free-form area that this group is in. Example: London.
        location (Any | Unset): The location that this group is in.  Must be geocodable. Example: College Road, London
            NW10 5EX, UK.
        country (Any | Unset): The free-form country (translated if translations are available in the current language).
            Example: United Kingdom.
        country_code (Any | Unset): The two-letter ISO country code. Example: GB.
        lat (Any | Unset): Latitude of the group. Example: 50.8113243.
        lng (Any | Unset): Longitude of the group. Example: -1.0788839.
        postcode (Any | Unset): The group postcode Example: SW9 7QD.
    """

    area: Any | Unset = UNSET
    location: Any | Unset = UNSET
    country: Any | Unset = UNSET
    country_code: Any | Unset = UNSET
    lat: Any | Unset = UNSET
    lng: Any | Unset = UNSET
    postcode: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        area = self.area

        location = self.location

        country = self.country

        country_code = self.country_code

        lat = self.lat

        lng = self.lng

        postcode = self.postcode

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if area is not UNSET:
            field_dict["area"] = area
        if location is not UNSET:
            field_dict["location"] = location
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if postcode is not UNSET:
            field_dict["postcode"] = postcode

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        area = d.pop("area", UNSET)

        location = d.pop("location", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("country_code", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        postcode = d.pop("postcode", UNSET)

        group_location = cls(
            area=area,
            location=location,
            country=country,
            country_code=country_code,
            lat=lat,
            lng=lng,
            postcode=postcode,
        )

        group_location.additional_properties = d
        return group_location

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
