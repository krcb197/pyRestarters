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

from ._base_client import APIBase
from .groups import Group
from .events import WithChildEvent

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

class Network(WithChildEvent):
    """
    A Network on the Restarters.net website
    """
    def __init__(self, network_id: int, network_payload:None|dict[str, Any] = None,
                 test_server:bool=False):
        """
        Initialise the class

        :param network_id: ID for the network
        :param network_payload: Dictionary of content for the event (assuming it has been
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
