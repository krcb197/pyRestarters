from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.network_stats import NetworkStats


T = TypeVar("T", bound="Network")


@_attrs_define
class Network:
    """A network of Groups using the Restarters platform.

    Attributes:
        id (Any): Unique identifier of this network Example: 1.
        name (Any | Unset): Unique name of this network Example: Default Network.
        logo (Any | Unset): URL of a logo for this network. Example:
            /mid_1597853610178a4b76e4d666b2a7b32ee75d8a24c706f1cbf213970.png.
        description (Any | Unset): HTML description of the network. Example: <p>This is a description.</p>.
        website (Any | Unset): An URL for the networks's own separate website. Example: https://therestartproject.org.
        shortname (Any | Unset): A short name for the network.. Example: resarters.
        default_language (Any | Unset): The default language for users in this network. Example: fr-BE.
        timezone (Any | Unset): Default timezone for this network. Example: Europe/London.
        stats (NetworkStats | Unset): An array of statistics about the activity of a network.
        updated_at (Any | Unset): The last change to this network.  This includes changes which affect the stats.
    """

    id: Any
    name: Any | Unset = UNSET
    logo: Any | Unset = UNSET
    description: Any | Unset = UNSET
    website: Any | Unset = UNSET
    shortname: Any | Unset = UNSET
    default_language: Any | Unset = UNSET
    timezone: Any | Unset = UNSET
    stats: NetworkStats | Unset = UNSET
    updated_at: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        logo = self.logo

        description = self.description

        website = self.website

        shortname = self.shortname

        default_language = self.default_language

        timezone = self.timezone

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if logo is not UNSET:
            field_dict["logo"] = logo
        if description is not UNSET:
            field_dict["description"] = description
        if website is not UNSET:
            field_dict["website"] = website
        if shortname is not UNSET:
            field_dict["shortname"] = shortname
        if default_language is not UNSET:
            field_dict["default_language"] = default_language
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if stats is not UNSET:
            field_dict["stats"] = stats
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.network_stats import NetworkStats

        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        logo = d.pop("logo", UNSET)

        description = d.pop("description", UNSET)

        website = d.pop("website", UNSET)

        shortname = d.pop("shortname", UNSET)

        default_language = d.pop("default_language", UNSET)

        timezone = d.pop("timezone", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: NetworkStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = NetworkStats.from_dict(_stats)

        updated_at = d.pop("updated_at", UNSET)

        network = cls(
            id=id,
            name=name,
            logo=logo,
            description=description,
            website=website,
            shortname=shortname,
            default_language=default_language,
            timezone=timezone,
            stats=stats,
            updated_at=updated_at,
        )

        network.additional_properties = d
        return network

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
