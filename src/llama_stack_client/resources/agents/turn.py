# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    required_args,
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.agents import turn_create_params
from ...types.agents.turn_create_response import TurnCreateResponse
from ...types.agents.turn_retrieve_response import TurnRetrieveResponse
from ...types.agents.agent_turn_response_stream_chunk import AgentTurnResponseStreamChunk

__all__ = ["TurnResource", "AsyncTurnResource"]


class TurnResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return TurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return TurnResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        stream: Literal[True],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[AgentTurnResponseStreamChunk]:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        stream: bool,
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse | Stream[AgentTurnResponseStreamChunk]:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "messages"], ["agent_id", "messages", "stream"])
    def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse | Stream[AgentTurnResponseStreamChunk]:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn",
            body=maybe_transform(
                {
                    "messages": messages,
                    "documents": documents,
                    "stream": stream,
                    "tool_config": tool_config,
                    "toolgroups": toolgroups,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnCreateResponse,
            stream=stream or False,
            stream_cls=Stream[AgentTurnResponseStreamChunk],
        )

    def retrieve(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnRetrieveResponse,
        )


class AsyncTurnResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTurnResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTurnResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTurnResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/llama-stack-python#with_streaming_response
        """
        return AsyncTurnResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        stream: Literal[True],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[AgentTurnResponseStreamChunk]:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        stream: bool,
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse | AsyncStream[AgentTurnResponseStreamChunk]:
        """
        Args:
          tool_config: Configuration for tool use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["agent_id", "messages"], ["agent_id", "messages", "stream"])
    async def create(
        self,
        session_id: str,
        *,
        agent_id: str,
        messages: Iterable[turn_create_params.Message],
        documents: Iterable[turn_create_params.Document] | NotGiven = NOT_GIVEN,
        stream: Literal[False] | Literal[True] | NotGiven = NOT_GIVEN,
        tool_config: turn_create_params.ToolConfig | NotGiven = NOT_GIVEN,
        toolgroups: List[turn_create_params.Toolgroup] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnCreateResponse | AsyncStream[AgentTurnResponseStreamChunk]:
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/v1/agents/{agent_id}/session/{session_id}/turn",
            body=await async_maybe_transform(
                {
                    "messages": messages,
                    "documents": documents,
                    "stream": stream,
                    "tool_config": tool_config,
                    "toolgroups": toolgroups,
                },
                turn_create_params.TurnCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnCreateResponse,
            stream=stream or False,
            stream_cls=AsyncStream[AgentTurnResponseStreamChunk],
        )

    async def retrieve(
        self,
        turn_id: str,
        *,
        agent_id: str,
        session_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TurnRetrieveResponse:
        """
        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not turn_id:
            raise ValueError(f"Expected a non-empty value for `turn_id` but received {turn_id!r}")
        return await self._get(
            f"/v1/agents/{agent_id}/session/{session_id}/turn/{turn_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TurnRetrieveResponse,
        )


class TurnResourceWithRawResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

        self.create = to_raw_response_wrapper(
            turn.create,
        )
        self.retrieve = to_raw_response_wrapper(
            turn.retrieve,
        )


class AsyncTurnResourceWithRawResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

        self.create = async_to_raw_response_wrapper(
            turn.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            turn.retrieve,
        )


class TurnResourceWithStreamingResponse:
    def __init__(self, turn: TurnResource) -> None:
        self._turn = turn

        self.create = to_streamed_response_wrapper(
            turn.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            turn.retrieve,
        )


class AsyncTurnResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTurnResource) -> None:
        self._turn = turn

        self.create = async_to_streamed_response_wrapper(
            turn.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            turn.retrieve,
        )
