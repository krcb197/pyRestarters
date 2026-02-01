from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event import Event
from ...types import UNSET, Response


def _get_kwargs(
    *,
    api_token: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["api_token"] = api_token

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/moderate/events",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> list[Event] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Event.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[list[Event]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_token: str,
) -> Response[list[Event]]:
    """Get Events for Moderation

     Only available for Administrators and Network Coordinators.

    Args:
        api_token (str):  Example: 1234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Event]]
    """

    kwargs = _get_kwargs(
        api_token=api_token,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    api_token: str,
) -> list[Event] | None:
    """Get Events for Moderation

     Only available for Administrators and Network Coordinators.

    Args:
        api_token (str):  Example: 1234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Event]
    """

    return sync_detailed(
        client=client,
        api_token=api_token,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    api_token: str,
) -> Response[list[Event]]:
    """Get Events for Moderation

     Only available for Administrators and Network Coordinators.

    Args:
        api_token (str):  Example: 1234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[list[Event]]
    """

    kwargs = _get_kwargs(
        api_token=api_token,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    api_token: str,
) -> list[Event] | None:
    """Get Events for Moderation

     Only available for Administrators and Network Coordinators.

    Args:
        api_token (str):  Example: 1234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        list[Event]
    """

    return (
        await asyncio_detailed(
            client=client,
            api_token=api_token,
        )
    ).parsed
