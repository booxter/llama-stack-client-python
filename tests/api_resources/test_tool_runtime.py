# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.shared import ToolDef, ToolInvocationResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolRuntime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_discover(self, client: LlamaStackClient) -> None:
        tool_runtime = client.tool_runtime.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        )
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_discover_with_all_params(self, client: LlamaStackClient) -> None:
        tool_runtime = client.tool_runtime.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_discover(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.with_raw_response.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = response.parse()
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_discover(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.with_streaming_response.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_runtime = response.parse()
            assert_matches_type(ToolDef, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_invoke(self, client: LlamaStackClient) -> None:
        tool_runtime = client.tool_runtime.invoke(
            args={"foo": True},
            tool_name="tool_name",
        )
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_method_invoke_with_all_params(self, client: LlamaStackClient) -> None:
        tool_runtime = client.tool_runtime.invoke(
            args={"foo": True},
            tool_name="tool_name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_raw_response_invoke(self, client: LlamaStackClient) -> None:
        response = client.tool_runtime.with_raw_response.invoke(
            args={"foo": True},
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = response.parse()
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    def test_streaming_response_invoke(self, client: LlamaStackClient) -> None:
        with client.tool_runtime.with_streaming_response.invoke(
            args={"foo": True},
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_runtime = response.parse()
            assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncToolRuntime:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_discover(self, async_client: AsyncLlamaStackClient) -> None:
        tool_runtime = await async_client.tool_runtime.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        )
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_runtime = await async_client.tool_runtime.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.with_raw_response.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = await response.parse()
        assert_matches_type(ToolDef, tool_runtime, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.with_streaming_response.discover(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_runtime = await response.parse()
            assert_matches_type(ToolDef, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_invoke(self, async_client: AsyncLlamaStackClient) -> None:
        tool_runtime = await async_client.tool_runtime.invoke(
            args={"foo": True},
            tool_name="tool_name",
        )
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_method_invoke_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_runtime = await async_client.tool_runtime.invoke(
            args={"foo": True},
            tool_name="tool_name",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_runtime.with_raw_response.invoke(
            args={"foo": True},
            tool_name="tool_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_runtime = await response.parse()
        assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_runtime.with_streaming_response.invoke(
            args={"foo": True},
            tool_name="tool_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_runtime = await response.parse()
            assert_matches_type(ToolInvocationResult, tool_runtime, path=["response"])

        assert cast(Any, response.is_closed) is True
