from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_summary import GroupSummary


T = TypeVar("T", bound="EventSummary")


@_attrs_define
class EventSummary:
    """The basic information about an event.  For full information, fetch the event.

    Attributes:
        id (Any): Unique identifier of this event Example: 1.
        summary (Any): Indicates that this is a summary result, not full group information. Example: true.
        start (Any | Unset): Start time of the event in ISO8601 format. Example: 2022-09-18T11:30:00+00:00.
        end (Any | Unset): End time of the event in ISO8601 format Example: 2022-09-18T12:30:00+00:00.
        timezone (Any | Unset): Timezone in which the event is taking place. Example: Europe/London.
        title (Any | Unset): Title of the event Example: Repair Cafe.
        location (Any | Unset): Human-readable address of the event Example: Village Hall, Main Street, Anytown, UK.
        online (Any | Unset): Whether this event is online (virtual). Example: false.
        lat (Any | Unset): Latitude at which the event is taking place.  Only valid if online=false. Example:
            50.8113243.
        lng (Any | Unset): Longitude at which the event is taking place.  Only valid if online=false. Example:
            -1.0788839.
        group (GroupSummary | Unset): The very basic information about a group.  For full information, fetch the group.
        approved (Any | Unset): Whether this event has been approved. Example: false.
        updated_at (Any | Unset): The last change to this group.  This includes changes which affect the stats.
    """

    id: Any
    summary: Any
    start: Any | Unset = UNSET
    end: Any | Unset = UNSET
    timezone: Any | Unset = UNSET
    title: Any | Unset = UNSET
    location: Any | Unset = UNSET
    online: Any | Unset = UNSET
    lat: Any | Unset = UNSET
    lng: Any | Unset = UNSET
    group: GroupSummary | Unset = UNSET
    approved: Any | Unset = UNSET
    updated_at: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        summary = self.summary

        start = self.start

        end = self.end

        timezone = self.timezone

        title = self.title

        location = self.location

        online = self.online

        lat = self.lat

        lng = self.lng

        group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group.to_dict()

        approved = self.approved

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "summary": summary,
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
        if location is not UNSET:
            field_dict["location"] = location
        if online is not UNSET:
            field_dict["online"] = online
        if lat is not UNSET:
            field_dict["lat"] = lat
        if lng is not UNSET:
            field_dict["lng"] = lng
        if group is not UNSET:
            field_dict["group"] = group
        if approved is not UNSET:
            field_dict["approved"] = approved
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_summary import GroupSummary

        d = dict(src_dict)
        id = d.pop("id")

        summary = d.pop("summary")

        start = d.pop("start", UNSET)

        end = d.pop("end", UNSET)

        timezone = d.pop("timezone", UNSET)

        title = d.pop("title", UNSET)

        location = d.pop("location", UNSET)

        online = d.pop("online", UNSET)

        lat = d.pop("lat", UNSET)

        lng = d.pop("lng", UNSET)

        _group = d.pop("group", UNSET)
        group: GroupSummary | Unset
        if isinstance(_group, Unset):
            group = UNSET
        else:
            group = GroupSummary.from_dict(_group)

        approved = d.pop("approved", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        event_summary = cls(
            id=id,
            summary=summary,
            start=start,
            end=end,
            timezone=timezone,
            title=title,
            location=location,
            online=online,
            lat=lat,
            lng=lng,
            group=group,
            approved=approved,
            updated_at=updated_at,
        )

        event_summary.additional_properties = d
        return event_summary

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
