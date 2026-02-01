from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_network_events_response_200 import GetNetworkEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    updated_start: str | Unset = UNSET,
    updated_end: str | Unset = UNSET,
    include_details: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["start"] = start

    params["end"] = end

    params["updated_start"] = updated_start

    params["updated_end"] = updated_end

    params["includeDetails"] = include_details

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/networks/{id}/events".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | GetNetworkEventsResponse200 | None:
    if response.status_code == 200:
        response_200 = GetNetworkEventsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | GetNetworkEventsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    updated_start: str | Unset = UNSET,
    updated_end: str | Unset = UNSET,
    include_details: bool | Unset = UNSET,
) -> Response[Any | GetNetworkEventsResponse200]:
    """Get Network Events

     Returns list of events for a network.

    Args:
        id (int):
        start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        updated_start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        updated_end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        include_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetNetworkEventsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        start=start,
        end=end,
        updated_start=updated_start,
        updated_end=updated_end,
        include_details=include_details,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    updated_start: str | Unset = UNSET,
    updated_end: str | Unset = UNSET,
    include_details: bool | Unset = UNSET,
) -> Any | GetNetworkEventsResponse200 | None:
    """Get Network Events

     Returns list of events for a network.

    Args:
        id (int):
        start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        updated_start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        updated_end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        include_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetNetworkEventsResponse200
    """

    return sync_detailed(
        id=id,
        client=client,
        start=start,
        end=end,
        updated_start=updated_start,
        updated_end=updated_end,
        include_details=include_details,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    updated_start: str | Unset = UNSET,
    updated_end: str | Unset = UNSET,
    include_details: bool | Unset = UNSET,
) -> Response[Any | GetNetworkEventsResponse200]:
    """Get Network Events

     Returns list of events for a network.

    Args:
        id (int):
        start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        updated_start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        updated_end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        include_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | GetNetworkEventsResponse200]
    """

    kwargs = _get_kwargs(
        id=id,
        start=start,
        end=end,
        updated_start=updated_start,
        updated_end=updated_end,
        include_details=include_details,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient | Client,
    start: str | Unset = UNSET,
    end: str | Unset = UNSET,
    updated_start: str | Unset = UNSET,
    updated_end: str | Unset = UNSET,
    include_details: bool | Unset = UNSET,
) -> Any | GetNetworkEventsResponse200 | None:
    """Get Network Events

     Returns list of events for a network.

    Args:
        id (int):
        start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        updated_start (str | Unset):  Example: 2022-09-18T11:30:00+00:00.
        updated_end (str | Unset):  Example: 2022-09-18T12:30:00+00:00.
        include_details (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | GetNetworkEventsResponse200
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            start=start,
            end=end,
            updated_start=updated_start,
            updated_end=updated_end,
            include_details=include_details,
        )
    ).parsed
