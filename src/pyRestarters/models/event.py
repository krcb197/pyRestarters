from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_stats import EventStats
    from ..models.group_summary import GroupSummary


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """The full information about an event.

    Attributes:
        id (Any): Unique identifier of this event Example: 1.
        full (Any): Indicates that this is a full result, not summary group information. Example: true.
        start (Any | Unset): Start time of the event in ISO8601 format. Example: 2022-09-18T11:30:00+00:00.
        end (Any | Unset): End time of the event in ISO8601 format Example: 2022-09-18T12:30:00+00:00.
        timezone (Any | Unset): Timezone in which the event is taking place. Example: Europe/London.
        title (Any | Unset): Title of the event Example: Europe/London.
        description (Any | Unset): A description of the event.  May contain HTML Example: Come along and we'll fix your
            broken electrical items..
        location (Any | Unset): Human-readable address of the event Example: Europe/London.
        lat (Any | Unset): Latitude at which the event is taking place.  Only valid if online=false. Example:
            50.8113243.
        online (Any | Unset): Whether this event is online (virtual). Example: false.
        lng (Any | Unset): Longitude at which the event is taking place.  Only valid if online=false. Example:
            -1.0788839.
        group (GroupSummary | Unset): The very basic information about a group.  For full information, fetch the group.
        link (str | Unset): Optional web link
        approved (bool | Unset): Whether the event has been approved
        network_data (Any | Unset): Network-defined JSON data
        stats (EventStats | Unset): An array of statistics about the activity of an event.
        updated_at (Any | Unset): The last change to this group.  This includes changes which affect the stats.
    """

    id: Any
    full: Any
    start: Any | Unset = UNSET
    end: Any | Unset = UNSET
    timezone: Any | Unset = UNSET
    title: Any | Unset = UNSET
    description: Any | Unset = UNSET
    location: Any | Unset = UNSET
    lat: Any | Unset = UNSET
    online: Any | Unset = UNSET
    lng: Any | Unset = UNSET
    group: GroupSummary | Unset = UNSET
    link: str | Unset = UNSET
    approved: bool | Unset = UNSET
    network_data: Any | Unset = UNSET
    stats: EventStats | Unset = UNSET
    updated_at: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        full = self.full

        start = self.start

        end = self.end

        timezone = self.timezone

        title = self.title

        description = self.description

        location = self.location

        lat = self.lat

        online = self.online

        lng = self.lng

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        link = self.link

        approved = self.approved

        network_data = self.network_data

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "full": full,
            }
        )
        if start is not UNSET:
            field_dict["start"] = start
        if end is not UNSET:
            field_dict["end"] = end
        if timezone is not UNSET:
            field_dict["timezone"] = timezone
        if title is not UNSET:
            field_dict["title"] = title
        if description is not UNSET:
            field_dict["description"] = description
        if location is not UNSET:
            field_dict["location"] = location
        if lat is not UNSET:
            field_dict["lat"] = lat
        if online is not UNSET:
            field_dict["online"] = online
        if lng is not UNSET:
            field_dict["lng"] = lng
        if group is not UNSET:
            field_dict["group"] = group
        if link is not UNSET:
            field_dict["link"] = link
        if approved is not UNSET:
            field_dict["approved"] = approved
        if network_data is not UNSET:
            field_dict["network_data"] = network_data
        if stats is not UNSET:
            field_dict["stats"] = stats
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_stats import EventStats
        from ..models.group_summary import GroupSummary

        d = dict(src_dict)
        id = d.pop("id")

        full = d.pop("full")

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        timezone = d.pop("timezone", UNSET)

        title = d.pop("title", UNSET)

        description = d.pop("description", UNSET)

        location = d.pop("location", UNSET)

        lat = d.pop("lat", UNSET)

        online = d.pop("online", UNSET)

        lng = d.pop("lng", UNSET)

        _group = d.pop("group", UNSET)
        group: GroupSummary | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GroupSummary.from_dict(_group)

        link = d.pop("link", UNSET)

        approved = d.pop("approved", UNSET)

        network_data = d.pop("network_data", UNSET)

        _stats = d.pop("stats", UNSET)
        stats: EventStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = EventStats.from_dict(_stats)

        updated_at = d.pop("updated_at", UNSET)

        event = cls(
            id=id,
            full=full,
            start=start,
            end=end,
            timezone=timezone,
            title=title,
            description=description,
            location=location,
            lat=lat,
            online=online,
            lng=lng,
            group=group,
            link=link,
            approved=approved,
            network_data=network_data,
            stats=stats,
            updated_at=updated_at,
        )

        event.additional_properties = d
        return event

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
