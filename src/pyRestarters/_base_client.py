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

import requests

class APIBase(ABC):
    """
    Base class for accessing parts of the API
    """

    @property
    def _end_point(self) -> str:
        return "https://restarters.net/api/v2"

    def _get_response(self, endpoint: str) -> dict[str, Any]:

        if endpoint == '':
            full_end_point = self._end_point
        else:
            full_end_point = self._end_point + '/' + endpoint

        response = requests.get(
            url=full_end_point,
            headers={"Accept": "application/json", },
            timeout=10.0
        )

        if not response.status_code == 200:
            raise RuntimeError(f'request failed with status code: {response.status_code}')

        return response.json()

    @abstractmethod
    def _refresh(self):
        """
        Refresh the payload data
        """
