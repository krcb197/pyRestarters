from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event import Event
    from ..models.event_summary import EventSummary


T = TypeVar("T", bound="GetNetworkEventsResponse200")


@_attrs_define
class GetNetworkEventsResponse200:
    """
    Attributes:
        data (list[Event | EventSummary] | Unset): An array of events
    """

    data: list[Event | EventSummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.event_summary import EventSummary

        data: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item: dict[str, Any]
                if isinstance(data_item_data, EventSummary):
                    data_item = data_item_data.to_dict()
                else:
                    data_item = data_item_data.to_dict()

                data.append(data_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event import Event
        from ..models.event_summary import EventSummary

        d = dict(src_dict)
        _data = d.pop("data", UNSET)
        data: list[Event | EventSummary] | Unset = UNSET
        if _data is not UNSET:
            data = []
            for data_item_data in _data:

                def _parse_data_item(data: object) -> Event | EventSummary:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        data_item_type_0 = EventSummary.from_dict(data)

                        return data_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = Event.from_dict(data)

                    return data_item_type_1

                data_item = _parse_data_item(data_item_data)

                data.append(data_item)

        get_network_events_response_200 = cls(
            data=data,
        )

        get_network_events_response_200.additional_properties = d
        return get_network_events_response_200

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
