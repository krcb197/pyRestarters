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

This module provides access to the events part of the API
"""
from typing import Any

from ._base_client import APIBase

class Event(APIBase):
    """
    Event on the Restarters.net website
    """


    def __init__(self, event_id: int, event_payload:None|dict[str, Any] = None):
        """
        Initialise the class

        :param event_id: Event ID
        :param event_payload: Dictionary of content for the event (assuming it has been
                              retrieved in a previous operation
        """

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
