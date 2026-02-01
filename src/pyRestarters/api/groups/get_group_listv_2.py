from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_group_listv_2_response_200 import GetGroupListv2Response200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    include_archived: bool | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["includeArchived"] = include_archived

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v2/groups/names",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetGroupListv2Response200 | None:
    if response.status_code == 200:
        response_200 = GetGroupListv2Response200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetGroupListv2Response200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> Response[GetGroupListv2Response200]:
    """Get list of group names

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupListv2Response200]
    """

    kwargs = _get_kwargs(
        include_archived=include_archived,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> GetGroupListv2Response200 | None:
    """Get list of group names

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupListv2Response200
    """

    return sync_detailed(
        client=client,
        include_archived=include_archived,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> Response[GetGroupListv2Response200]:
    """Get list of group names

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetGroupListv2Response200]
    """

    kwargs = _get_kwargs(
        include_archived=include_archived,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    include_archived: bool | Unset = UNSET,
) -> GetGroupListv2Response200 | None:
    """Get list of group names

    Args:
        include_archived (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetGroupListv2Response200
    """

    return (
        await asyncio_detailed(
            client=client,
            include_archived=include_archived,
        )
    ).parsed
