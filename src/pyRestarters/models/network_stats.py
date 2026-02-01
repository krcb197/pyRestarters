from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetworkStats")


@_attrs_define
class NetworkStats:
    """An array of statistics about the activity of a network.

    Attributes:
        co2_powered (float | Unset): The amount of CO2 saved by repairing powered items.
        co2_unpowered (float | Unset): The amount of CO2 saved by repairing unpowered items.
        co2_total (float | Unset): co2_powered + co2_unpowered
        waste_powered (float | Unset): The weight in kg of waste saved by repairing powered items.
        waste_unpowered (float | Unset): The weight in kg of waste saved by repairing unpowered items.
        fixed_powered (float | Unset): The number of powered items which have been repaired.
        fixed_unpowered (float | Unset): The number of unpowered items which have been repaired.
        fixed_devices (float | Unset): fixed_powered + fixed_unpowered
        repairable_devices (float | Unset): The number of devices which were capable of being repaired.
        dead_devices (float | Unset): The number of devices which were not capable of being repaired.
        unknown_repair_status (float | Unset): The number of devices where the repair status was not known.
        devices_powered (float | Unset): The number of powered devices seen.
        devices_unpowered (float | Unset): The number of unpowered devices seen.
        no_weight_powered (float | Unset): The number of powered devices where no weight was provided.
        no_weight_unpowered (float | Unset): The number of unpowered devices where no weight was provided.
        participants (float | Unset): The number of people who attended.
        volunteers (float | Unset): The number of volunteers.
        hours_volunteered (float | Unset): The estimated number of hours volunteered for this network.
        events (float | Unset): The number of events created by this network.
        full (Any | Unset): Indicates that this is a full result, not summary network information. Example: true.
    """

    co2_powered: float | Unset = UNSET
    co2_unpowered: float | Unset = UNSET
    co2_total: float | Unset = UNSET
    waste_powered: float | Unset = UNSET
    waste_unpowered: float | Unset = UNSET
    fixed_powered: float | Unset = UNSET
    fixed_unpowered: float | Unset = UNSET
    fixed_devices: float | Unset = UNSET
    repairable_devices: float | Unset = UNSET
    dead_devices: float | Unset = UNSET
    unknown_repair_status: float | Unset = UNSET
    devices_powered: float | Unset = UNSET
    devices_unpowered: float | Unset = UNSET
    no_weight_powered: float | Unset = UNSET
    no_weight_unpowered: float | Unset = UNSET
    participants: float | Unset = UNSET
    volunteers: float | Unset = UNSET
    hours_volunteered: float | Unset = UNSET
    events: float | Unset = UNSET
    full: Any | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        co2_powered = self.co2_powered

        co2_unpowered = self.co2_unpowered

        co2_total = self.co2_total

        waste_powered = self.waste_powered

        waste_unpowered = self.waste_unpowered

        fixed_powered = self.fixed_powered

        fixed_unpowered = self.fixed_unpowered

        fixed_devices = self.fixed_devices

        repairable_devices = self.repairable_devices

        dead_devices = self.dead_devices

        unknown_repair_status = self.unknown_repair_status

        devices_powered = self.devices_powered

        devices_unpowered = self.devices_unpowered

        no_weight_powered = self.no_weight_powered

        no_weight_unpowered = self.no_weight_unpowered

        participants = self.participants

        volunteers = self.volunteers

        hours_volunteered = self.hours_volunteered

        events = self.events

        full = self.full

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if co2_powered is not UNSET:
            field_dict["co2_powered"] = co2_powered
        if co2_unpowered is not UNSET:
            field_dict["co2_unpowered"] = co2_unpowered
        if co2_total is not UNSET:
            field_dict["co2_total"] = co2_total
        if waste_powered is not UNSET:
            field_dict["waste_powered"] = waste_powered
        if waste_unpowered is not UNSET:
            field_dict["waste_unpowered"] = waste_unpowered
        if fixed_powered is not UNSET:
            field_dict["fixed_powered"] = fixed_powered
        if fixed_unpowered is not UNSET:
            field_dict["fixed_unpowered"] = fixed_unpowered
        if fixed_devices is not UNSET:
            field_dict["fixed_devices"] = fixed_devices
        if repairable_devices is not UNSET:
            field_dict["repairable_devices"] = repairable_devices
        if dead_devices is not UNSET:
            field_dict["dead_devices"] = dead_devices
        if unknown_repair_status is not UNSET:
            field_dict["unknown_repair_status"] = unknown_repair_status
        if devices_powered is not UNSET:
            field_dict["devices_powered"] = devices_powered
        if devices_unpowered is not UNSET:
            field_dict["devices_unpowered"] = devices_unpowered
        if no_weight_powered is not UNSET:
            field_dict["no_weight_powered"] = no_weight_powered
        if no_weight_unpowered is not UNSET:
            field_dict["no_weight_unpowered"] = no_weight_unpowered
        if participants is not UNSET:
            field_dict["participants"] = participants
        if volunteers is not UNSET:
            field_dict["volunteers"] = volunteers
        if hours_volunteered is not UNSET:
            field_dict["hours_volunteered"] = hours_volunteered
        if events is not UNSET:
            field_dict["events"] = events
        if full is not UNSET:
            field_dict["full"] = full

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        co2_powered = d.pop("co2_powered", UNSET)

        co2_unpowered = d.pop("co2_unpowered", UNSET)

        co2_total = d.pop("co2_total", UNSET)

        waste_powered = d.pop("waste_powered", UNSET)

        waste_unpowered = d.pop("waste_unpowered", UNSET)

        fixed_powered = d.pop("fixed_powered", UNSET)

        fixed_unpowered = d.pop("fixed_unpowered", UNSET)

        fixed_devices = d.pop("fixed_devices", UNSET)

        repairable_devices = d.pop("repairable_devices", UNSET)

        dead_devices = d.pop("dead_devices", UNSET)

        unknown_repair_status = d.pop("unknown_repair_status", UNSET)

        devices_powered = d.pop("devices_powered", UNSET)

        devices_unpowered = d.pop("devices_unpowered", UNSET)

        no_weight_powered = d.pop("no_weight_powered", UNSET)

        no_weight_unpowered = d.pop("no_weight_unpowered", UNSET)

        participants = d.pop("participants", UNSET)

        volunteers = d.pop("volunteers", UNSET)

        hours_volunteered = d.pop("hours_volunteered", UNSET)

        events = d.pop("events", UNSET)

        full = d.pop("full", UNSET)

        network_stats = cls(
            co2_powered=co2_powered,
            co2_unpowered=co2_unpowered,
            co2_total=co2_total,
            waste_powered=waste_powered,
            waste_unpowered=waste_unpowered,
            fixed_powered=fixed_powered,
            fixed_unpowered=fixed_unpowered,
            fixed_devices=fixed_devices,
            repairable_devices=repairable_devices,
            dead_devices=dead_devices,
            unknown_repair_status=unknown_repair_status,
            devices_powered=devices_powered,
            devices_unpowered=devices_unpowered,
            no_weight_powered=no_weight_powered,
            no_weight_unpowered=no_weight_unpowered,
            participants=participants,
            volunteers=volunteers,
            hours_volunteered=hours_volunteered,
            events=events,
            full=full,
        )

        network_stats.additional_properties = d
        return network_stats

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
