from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_summary import EventSummary
    from ..models.group_location import GroupLocation
    from ..models.network_summary import NetworkSummary


T = TypeVar("T", bound="GroupSummary")


@_attrs_define
class GroupSummary:
    """The very basic information about a group.  For full information, fetch the group.

    Attributes:
        id (Any): Unique identifier of this group Example: 1.
        summary (Any): Indicates that this is a summary result, not full group information. Example: true.
        name (Any | Unset): Unique name of this group Example: Restarters HQ.
        image (Any | Unset): URL of an image for this group.  You should prefix this with /uploads before use. Example:
            /mid_1597853610178a4b76e4d666b2a7b32ee75d8a24c706f1cbf213970.png.
        location (GroupLocation | Unset): The information about the location of a group.
        networks (list[NetworkSummary] | Unset): An array of networks of which the group is a member.
        updated_at (Any | Unset): The last change to this group.  This includes changes which affect the stats.
        next_event (EventSummary | Unset): The basic information about an event.  For full information, fetch the event.
        archived_at (Any | Unset): If present, this group has been archived and is no longer active.
    """

    id: Any
    summary: Any
    name: Any | Unset = UNSET
    image: Any | Unset = UNSET
    location: GroupLocation | Unset = UNSET
    networks: list[NetworkSummary] | Unset = UNSET
    updated_at: Any | Unset = UNSET
    next_event: EventSummary | Unset = UNSET
    archived_at: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        summary = self.summary

        name = self.name

        image = self.image

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        updated_at = self.updated_at

        next_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_event, Unset):
            next_event = self.next_event.to_dict()

        archived_at = self.archived_at

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
        if image is not UNSET:
            field_dict["image"] = image
        if location is not UNSET:
            field_dict["location"] = location
        if networks is not UNSET:
            field_dict["networks"] = networks
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if next_event is not UNSET:
            field_dict["next_event"] = next_event
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_summary import EventSummary
        from ..models.group_location import GroupLocation
        from ..models.network_summary import NetworkSummary

        d = dict(src_dict)
        id = d.pop("id")

        summary = d.pop("summary")

        name = d.pop("name", UNSET)

        image = d.pop("image", UNSET)

        _location = d.pop("location", UNSET)
        location: GroupLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GroupLocation.from_dict(_location)

        _networks = d.pop("networks", UNSET)
        networks: list[NetworkSummary] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = NetworkSummary.from_dict(networks_item_data)

                networks.append(networks_item)

        updated_at = d.pop("updated_at", UNSET)

        _next_event = d.pop("next_event", UNSET)
        next_event: EventSummary | Unset
        if isinstance(_next_event, Unset):
            next_event = UNSET
        else:
            next_event = EventSummary.from_dict(_next_event)

        archived_at = d.pop("archived_at", UNSET)

        group_summary = cls(
            id=id,
            summary=summary,
            name=name,
            image=image,
            location=location,
            networks=networks,
            updated_at=updated_at,
            next_event=next_event,
            archived_at=archived_at,
        )

        group_summary.additional_properties = d
        return group_summary

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
