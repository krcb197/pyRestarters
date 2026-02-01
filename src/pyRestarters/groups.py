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

This module provides access to the groups and groups part of the API
"""
from ._base_client import APIBase
from .events import Event, WithChildEvent

#pylint:disable-next=too-few-public-methods
class Groups(APIBase):
    """
    All the groups on the Restarters.net website
    """
    def __init__(self, include_archived:bool=False, test_server:bool=False):
        """
        Initialise the class

        :param include_archived: whether to include archived groups
        """
        super().__init__(test_server=test_server)
        self.__include_archived = include_archived


    @property
    def _end_point(self) -> str:
        return super()._end_point + '/groups'

    @property
    def names(self) -> dict[int, str]:
        """
        All the groups presented as a dictionary with the group ID as key
        """
        response = self._get_response(
            f'names?includeArchived={str(self.__include_archived).lower()}')

        return { item['id'] : item['name'] for item in response['data'] }

    def _refresh(self) -> None:
        raise NotImplementedError('groups do not have base data')

class Group(WithChildEvent):
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
    def next_event(self) -> Event:
        """
        Next event
        """
        next_event_id = self.__data['next_event']['id']
        return Event(event_id=next_event_id, test_server=self._test_server)


    def _refresh(self) -> None:
        response = self._get_response('')
        self.__data = response['data']
