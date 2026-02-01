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

This module provides the common access compontents to be used by the other classes
"""

from abc import ABC, abstractmethod
from typing import Any
from datetime import datetime

import requests

#pylint:disable-next=too-few-public-methods
class APIBase(ABC):
    """
    Base class for accessing parts of the API
    """
    def __init__(self, test_server:bool=False):
        self.__test_server = test_server

    @property
    def _end_point(self) -> str:
        if self._test_server:
            return "http://restarters.test:8000"

        return "https://restarters.net/api/v2"

    @property
    def _test_server(self):
        return self.__test_server

    def _get_response(self, endpoint: str) -> dict[str, Any]:

        if endpoint == '':
            full_end_point = self._end_point
        else:
            full_end_point = self._end_point + '/' + endpoint

        response = requests.get(
            url=full_end_point,
            headers={"Accept": "application/json", },
            timeout=self._request_get_timeout
        )

        if not response.status_code == 200:
            raise RuntimeError(f'request failed with status code: {response.status_code}')

        return response.json()

    @abstractmethod
    def _refresh(self) -> None:
        """
        Refresh the payload data
        """

    @property
    def _request_get_timeout(self) -> float:
        return 10.0

    @staticmethod
    def _datetime_from_json(data:str) -> datetime:
        """
        convert the isoformat datetime from the json content to a python object
        """
        return datetime.fromisoformat(data)
