from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_summary import EventSummary
    from ..models.group_location import GroupLocation
    from ..models.group_stats import GroupStats
    from ..models.network_summary import NetworkSummary
    from ..models.tag import Tag


T = TypeVar("T", bound="Group")


@_attrs_define
class Group:
    """A Group of Restarters, who organise events.

    Attributes:
        id (Any): Unique identifier of this group Example: 1.
        full (Any): Indicates that this is a full result, not summary group information. Example: true.
        name (Any | Unset): Unique name of this group Example: Restarters HQ.
        location (GroupLocation | Unset): The information about the location of a group.
        image (Any | Unset): URL of an image for this group.  You should prefix this with /uploads before use. Example:
            /mid_1597853610178a4b76e4d666b2a7b32ee75d8a24c706f1cbf213970.png.
        phone (Any | Unset): An optional phone number to contact the group. Example: 07544 314678.
        website (Any | Unset): An URL for the group's own separate website. Example: https://therestartproject.org.
        email (Any | Unset): Any email contact address for the group. Example: info@therestartproject.org.
        description (Any | Unset): HTML description of the group. Example: <p>This is a description.</p>.
        next_event (EventSummary | Unset): The basic information about an event.  For full information, fetch the event.
        timezone (Any | Unset): Timezone for this group.  If empty will inherit the timezone from the network. Example:
            Europe/London.
        hosts (float | Unset): The number of hosts of this group.
        restarters (float | Unset): The number of restarters in this group.
        approved (bool | Unset): Whether the group has been approved
        networks (list[NetworkSummary] | Unset): An array of networks of which the group is a member.
        tags (list[Tag] | Unset): An array of tags which apply to the group.
        network_data (Any | Unset): Network-defined JSON data
        stats (GroupStats | Unset): An array of statistics about the activity of a group.
        updated_at (Any | Unset): The last change to this group.  This includes changes which affect the stats.
        archived_at (Any | Unset): If present, this group has been archived and is no longer active.
    """

    id: Any
    full: Any
    name: Any | Unset = UNSET
    location: GroupLocation | Unset = UNSET
    image: Any | Unset = UNSET
    phone: Any | Unset = UNSET
    website: Any | Unset = UNSET
    email: Any | Unset = UNSET
    description: Any | Unset = UNSET
    next_event: EventSummary | Unset = UNSET
    timezone: Any | Unset = UNSET
    hosts: float | Unset = UNSET
    restarters: float | Unset = UNSET
    approved: bool | Unset = UNSET
    networks: list[NetworkSummary] | Unset = UNSET
    tags: list[Tag] | Unset = UNSET
    network_data: Any | Unset = UNSET
    stats: GroupStats | Unset = UNSET
    updated_at: Any | Unset = UNSET
    archived_at: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        full = self.full

        name = self.name

        location: dict[str, Any] | Unset = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        image = self.image

        phone = self.phone

        website = self.website

        email = self.email

        description = self.description

        next_event: dict[str, Any] | Unset = UNSET
        if not isinstance(self.next_event, Unset):
            next_event = self.next_event.to_dict()

        timezone = self.timezone

        hosts = self.hosts

        restarters = self.restarters

        approved = self.approved

        networks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.networks, Unset):
            networks = []
            for networks_item_data in self.networks:
                networks_item = networks_item_data.to_dict()
                networks.append(networks_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        network_data = self.network_data

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        updated_at = self.updated_at

        archived_at = self.archived_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "full": full,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if location is not UNSET:
            field_dict["location"] = location
        if image is not UNSET:
            field_dict["image"] = image
        if phone is not UNSET:
            field_dict["phone"] = phone
        if website is not UNSET:
            field_dict["website"] = website
        if email is not UNSET:
            field_dict["email"] = email
        if description is not UNSET:
            field_dict["description"] = description
        if next_event is not UNSET:
            field_dict["next_event"] = next_event
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if hosts is not UNSET:
            field_dict["hosts"] = hosts
        if restarters is not UNSET:
            field_dict["restarters"] = restarters
        if approved is not UNSET:
            field_dict["approved"] = approved
        if networks is not UNSET:
            field_dict["networks"] = networks
        if tags is not UNSET:
            field_dict["tags"] = tags
        if network_data is not UNSET:
            field_dict["network_data"] = network_data
        if stats is not UNSET:
            field_dict["stats"] = stats
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if archived_at is not UNSET:
            field_dict["archived_at"] = archived_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_summary import EventSummary
        from ..models.group_location import GroupLocation
        from ..models.group_stats import GroupStats
        from ..models.network_summary import NetworkSummary
        from ..models.tag import Tag

        d = dict(src_dict)
        id = d.pop("id")

        full = d.pop("full")

        name = d.pop("name", UNSET)

        _location = d.pop("location", UNSET)
        location: GroupLocation | Unset
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = GroupLocation.from_dict(_location)

        image = d.pop("image", UNSET)

        phone = d.pop("phone", UNSET)

        website = d.pop("website", UNSET)

        email = d.pop("email", UNSET)

        description = d.pop("description", UNSET)

        _next_event = d.pop("next_event", UNSET)
        next_event: EventSummary | Unset
        if isinstance(_next_event, Unset):
            next_event = UNSET
        else:
            next_event = EventSummary.from_dict(_next_event)

        timezone = d.pop("timezone", UNSET)

        hosts = d.pop("hosts", UNSET)

        restarters = d.pop("restarters", UNSET)

        approved = d.pop("approved", UNSET)

        _networks = d.pop("networks", UNSET)
        networks: list[NetworkSummary] | Unset = UNSET
        if _networks is not UNSET:
            networks = []
            for networks_item_data in _networks:
                networks_item = NetworkSummary.from_dict(networks_item_data)

                networks.append(networks_item)

        _tags = d.pop("tags", UNSET)
        tags: list[Tag] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = Tag.from_dict(tags_item_data)

                tags.append(tags_item)

        network_data = d.pop("network_data", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: GroupStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = GroupStats.from_dict(_stats)

        updated_at = d.pop("updated_at", UNSET)

        archived_at = d.pop("archived_at", UNSET)

        group = cls(
            id=id,
            full=full,
            name=name,
            location=location,
            image=image,
            phone=phone,
            website=website,
            email=email,
            description=description,
            next_event=next_event,
            timezone=timezone,
            hosts=hosts,
            restarters=restarters,
            approved=approved,
            networks=networks,
            tags=tags,
            network_data=network_data,
            stats=stats,
            updated_at=updated_at,
            archived_at=archived_at,
        )

        group.additional_properties = d
        return group

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
