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

This module provides access to the Networks and Network part of the API
"""
from typing import Any
import datetime
import urllib.parse

from ._base_client import APIBase
from .events import Event
from .groups import Group

#pylint:disable-next=too-few-public-methods
class Networks(APIBase):
    """
    All the networks on the Restarters.net website
    """


    def __init__(self, include_archived:bool=False):
        """
        Initialise the class
        """
        self.__include_archived = include_archived


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

class Network(APIBase):
    """
    A Network on the Restarters.net website
    """
    def __init__(self, network_id: int, network_payload:None|dict[str, Any] = None):
        """
        Initialise the class

        :param network_id: ID for the network
        :param network_payload: Dictionary of content for the event (assuming it has been
                                retrieved in a previous operation
        """

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
    def events(self) -> dict[int, Event]:
        """
        Network Events
        """
        response = self._get_response('events')
        return {item['id']: Event(event_id=item['id'], event_payload=item)
                for item in response['data']}

    @property
    def groups(self) -> dict[int, Group]:
        """
        Network Events
        """
        response = self._get_response('groups')
        return {item['id']: Group(event_id=item['id'], event_payload=item)
                for item in response['data']}

    @property
    def past_events(self) -> dict[int, Event]:
        """
        Past events for the Network
        """
        now = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0)
        response = self._get_response(f'events?end={urllib.parse.quote_plus(now.isoformat())}')
        return { item['id'] : Event(event_id=item['id'], event_payload=item)
                 for item in response['data']}

    @property
    def future_events(self) -> dict[int, Event]:
        """
        Future events for the Network
        """
        now = datetime.datetime.now(tz=datetime.timezone.utc).replace(microsecond=0)
        response = self._get_response(f'events?start={urllib.parse.quote_plus(now.isoformat())}')
        return { item['id'] : Event(event_id=item['id'], event_payload=item)
                 for item in response['data']}

    def _refresh(self) -> None:
        response = self._get_response('')
        self.__data = response['data']
