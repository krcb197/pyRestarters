"""
pyRestarters is a python wrapper for the restarters.net API
Copyright (C) 2026

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

This module provides access to the events, groups and groups part of the API
"""
from functools import cached_property
from collections.abc import Iterator
from typing import Any, NamedTuple
import datetime
from dataclasses import dataclass

import urllib.parse
from abc import ABC

from ._base_client import APIBase

class LocationCoordinates(NamedTuple):
    """
    Tuple for latitude and longitude
    """
    latitude: float
    longitude: float

class Event(APIBase):
    """
    Event on the Restarters.net website
    """

    def __init__(self, event_id: int, event_payload: None | dict[str, Any] = None,
                 test_server: bool = False):
        """
        Initialise the class

        :param event_id: Event ID
        :param event_payload: Dictionary of content for the event (assuming it has been
                              retrieved in a previous operation
        """
        super().__init__(test_server=test_server)

        self.__event_id = event_id
        if event_payload is None:
            self._refresh()
        else:
            self.__data = event_payload

    @property
    def event_id(self) -> int:
        """
        Event ID
        """
        return self.__event_id

    @property
    def _end_point(self) -> str:
        return super()._end_point + '/events/' + f'{self.__event_id}'

    def _refresh(self) -> None:
        response = self._get_response('')
        self.__data = response['data']

    @property
    def title(self) -> str:
        """
        Event Title
        """
        return self.__data['title']

    @property
    def start(self) -> datetime.datetime:
        """
        Start date and time for the event
        """
        start_str = self.__data['start']
        return self._datetime_from_json(start_str)

    @property
    def end_at(self) -> datetime.datetime:
        """
        End date and time for the event
        """
        end_str = self.__data['end']
        return self._datetime_from_json(end_str)

    @property
    def group(self) -> "Group":
        """
        Group organising the event
        """
        return Group(group_id=self.__data['group']['id'])

    @property
    def coordinates(self) -> LocationCoordinates:
        """
        Location of the event
        """
        lng = self.__data['lng']
        lat = self.__data['lat']
        return LocationCoordinates(longitude=lng, latitude=lat)


class _WithChildEvent(APIBase, ABC):
    """
    A object in the data model that has child events
    """

    @property
    def events(self) -> dict[int, Event]:
        """
        Events
        """
        return self.events_in_daterange(start=None, end=None)

    @property
    def past_events(self) -> dict[int, Event]:
        """
        Past events

        Returns:
            A dictionary of events with the event ID as the key
        """
        now = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0)
        return self.events_in_daterange(start=None, end=now)

    @property
    def future_events(self) -> dict[int, Event]:
        """
        Future events

        Returns:
            A dictionary of events with the event ID as the key
        """
        now = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0)
        return self.events_in_daterange(start=now, end=None)

    def events_in_daterange(self,
                            start:datetime.datetime|None,
                            end:datetime.datetime|None) -> dict[int, Event]:
        """
        Provide all the events in a date range. Setting either Start or End to None will
        remove that filter

        Returns:
            A dictionary of events with the event ID as the key
        """
        if start is None and end is not None:
            query_str=f'events?end={urllib.parse.quote_plus(end.isoformat())}'
        elif start is not None and end is None:
            query_str=f'events?start={urllib.parse.quote_plus(start.isoformat())}'
        elif start is not None and end is not None:
            query_str=(f'events?start={urllib.parse.quote_plus(start.isoformat())}'
                       f'&end={urllib.parse.quote_plus(end.isoformat())}')
        else:
            query_str = 'events'

        response = self._get_response(query_str)
        return {item['id']: Event(event_id=item['id'], event_payload=item,
                                  test_server=self._test_server)
                for item in response['data']}

@dataclass(frozen=True)
class GroupTag:
    """
    Data class to hold an tag
    """
    id : int
    name : str
    description : str

class Group(_WithChildEvent):
    """
    A group on the Restarters.net website
    """
    def __init__(self, group_id: int, test_server:bool=False):
        """
        Initialise the close

        :param group_id: ID for the group
        """
        super().__init__(test_server=test_server)

        self.__group_id = group_id
        self._refresh()


    @property
    def group_id(self) -> int:
        """
        Group ID
        """
        return self.__group_id

    @property
    def name(self) -> str:
        """
        Group Name
        """
        return self.__data['name']

    @property
    def description(self) -> str:
        """
        Group Description
        """
        return self.__data['description']

    @property
    def _end_point(self) -> str:
        return super()._end_point + '/groups/' + f'{self.group_id}'

    @property
    def next_event(self) -> None | Event:
        """
        Next event
        """
        if 'next_event' not in self.__data:
            return None

        next_event_id = self.__data['next_event']['id']
        return Event(event_id=next_event_id, test_server=self._test_server)


    def _refresh(self) -> None:
        response = self._get_response('')
        self.__data = response['data']

    @property
    def tags(self) -> list[GroupTag]:
        """
        The tags for the group
        """
        tags = self.__data['tags']
        return [GroupTag(id=tag['id'], name=tag['name'], description=tag['description'])
                for tag in tags]

    @property
    def website(self) -> str:
        """
        Group Description
        """
        return self.__data['website']

    @property
    def email(self) -> str:
        """
        Group Description
        """
        return self.__data['email']

    @property
    def postal_address(self) -> str:
        """
        Group Description
        """
        return self.__data['location']['location']

    @property
    def postcode(self) -> str:
        """
        Group Description
        """
        return self.__data['location']['postcode']



class Groups(APIBase):
    """
    All the groups on the Restarters.net website
    """
    def __init__(self, include_archived:bool=False, test_server:bool=False):
        """
        All the groups on the Restarters.net website

        Args
            include_archived: whether to include archived groups
            test_server: whether to use the test server (as opposed to the live server)
        """
        super().__init__(test_server=test_server)
        self.__include_archived = include_archived


    @property
    def _end_point(self) -> str:
        return super()._end_point + '/groups'

    @cached_property
    def names(self) -> dict[int, str]:
        """
        All the groups presented as a dictionary with the group ID as key

        .. note :: This property is cached and only retrieved once per session
        """
        response = self._get_response(
            f'names?includeArchived={str(self.__include_archived).lower()}')

        return { item['id'] : item['name'] for item in response['data'] }

    @property
    def _id_by_name(self) -> dict[str, int]:
        """
        All the groups ID presented as a dictionary with the name as a key. This is useful
        for looking up the ID of a group
        """
        return {v: k for k, v in self.names.items()}

    def group_by_name(self, group_name: str) -> None | Group:
        """
        Return a group by its name

        Args:
            group_name: name of the group e.g. Repair Café Gosport

        Returns:
            A group object
        """
        group_id = self._id_by_name.get(group_name, None)
        if group_id is None:
            return None
        return Group(group_id=group_id)

    @property
    def group_tags(self) -> list[GroupTag]:
        """
        All the possible group tags
        """
        response = self._get_response('tags')
        return [GroupTag(id=tag['id'], name=tag['name'], description=tag['description'])
                for tag in response['data']]


    def __iter__(self) -> Iterator[Group]:
        for group_id in self.names.keys():
            yield Group(group_id=group_id)

    def _refresh(self) -> None:
        raise NotImplementedError('groups do not have base data')

#pylint:disable-next=too-few-public-methods
class Networks(APIBase):
    """
    All the networks on the Restarters.net website
    """

    @property
    def _end_point(self) -> str:
        return super()._end_point + '/networks'

    @property
    def networks(self) -> dict[int, 'Network']:
        """
        All the groups presented as a dictionary with the network ID as key
        """
        response = self._get_response('')

        return { item['id'] : Network(network_id=item['id'],network_payload=item)
                 for item in response['data'] }

    def _refresh(self) -> None:
        raise NotImplementedError('groups do not have base data')

class Network(_WithChildEvent):
    """
    A Network on the Restarters.net website
    """
    def __init__(self, network_id: int, network_payload:None|dict[str, Any] = None,
                 test_server:bool=False):
        """
        Initialise the class

        Args:
            network_id: ID for the network
            network_payload: Dictionary of content for the event (assuming it has been
                             retrieved in a previous operation
        """
        super().__init__(test_server=test_server)

        self.__network_id = network_id
        if network_payload is None:
            self._refresh()
        else:
            self.__data = network_payload


    @property
    def network_id(self) -> int:
        """
        Network ID
        """
        return self.__network_id

    @property
    def name(self) -> str:
        """
        Group Name
        """
        return self.__data['name']

    @property
    def description(self) -> str:
        """
        Group Description
        """
        return self.__data['description']

    @property
    def _end_point(self) -> str:
        return super()._end_point + '/networks/' + f'{self.network_id}'

    @property
    def groups(self) -> dict[int, Group]:
        """
        Network Events
        """
        response = self._get_response('groups')
        return {item['id']: Group(group_id=item['id'])
                for item in response['data']}

    def _refresh(self) -> None:
        response = self._get_response('')
        self.__data = response['data']

    @property
    def _request_get_timeout(self) -> float:
        return 60.0
