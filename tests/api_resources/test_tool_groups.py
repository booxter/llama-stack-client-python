# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from llama_stack_client import LlamaStackClient, AsyncLlamaStackClient
from llama_stack_client.types.shared import ToolGroup

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToolGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.list()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_raw_response_list(self, client: LlamaStackClient) -> None:
        response = client.tool_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = response.parse()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    def test_streaming_response_list(self, client: LlamaStackClient) -> None:
        with client.tool_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = response.parse()
            assert_matches_type(ToolGroup, tool_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.get(
            tool_group_id="tool_group_id",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.get(
            tool_group_id="tool_group_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: LlamaStackClient) -> None:
        response = client.tool_groups.with_raw_response.get(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = response.parse()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: LlamaStackClient) -> None:
        with client.tool_groups.with_streaming_response.get(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = response.parse()
            assert_matches_type(ToolGroup, tool_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        )
        assert tool_group is None

    @parametrize
    def test_method_register_with_all_params(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
            provider_id="provider_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert tool_group is None

    @parametrize
    def test_raw_response_register(self, client: LlamaStackClient) -> None:
        response = client.tool_groups.with_raw_response.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = response.parse()
        assert tool_group is None

    @parametrize
    def test_streaming_response_register(self, client: LlamaStackClient) -> None:
        with client.tool_groups.with_streaming_response.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = response.parse()
            assert tool_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_unregister(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.unregister(
            tool_group_id="tool_group_id",
        )
        assert tool_group is None

    @parametrize
    def test_method_unregister_with_all_params(self, client: LlamaStackClient) -> None:
        tool_group = client.tool_groups.unregister(
            tool_group_id="tool_group_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert tool_group is None

    @parametrize
    def test_raw_response_unregister(self, client: LlamaStackClient) -> None:
        response = client.tool_groups.with_raw_response.unregister(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = response.parse()
        assert tool_group is None

    @parametrize
    def test_streaming_response_unregister(self, client: LlamaStackClient) -> None:
        with client.tool_groups.with_streaming_response.unregister(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = response.parse()
            assert tool_group is None

        assert cast(Any, response.is_closed) is True


class TestAsyncToolGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.list()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.list(
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_groups.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = await response.parse()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints with content type application/jsonl, Prism mock server will fail"
    )
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_groups.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = await response.parse()
            assert_matches_type(ToolGroup, tool_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.get(
            tool_group_id="tool_group_id",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.get(
            tool_group_id="tool_group_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_groups.with_raw_response.get(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = await response.parse()
        assert_matches_type(ToolGroup, tool_group, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_groups.with_streaming_response.get(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = await response.parse()
            assert_matches_type(ToolGroup, tool_group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        )
        assert tool_group is None

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
            provider_id="provider_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert tool_group is None

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_groups.with_raw_response.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = await response.parse()
        assert tool_group is None

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_groups.with_streaming_response.register(
            tool_group={
                "endpoint": {"uri": "uri"},
                "type": "model_context_protocol",
            },
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = await response.parse()
            assert tool_group is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.unregister(
            tool_group_id="tool_group_id",
        )
        assert tool_group is None

    @parametrize
    async def test_method_unregister_with_all_params(self, async_client: AsyncLlamaStackClient) -> None:
        tool_group = await async_client.tool_groups.unregister(
            tool_group_id="tool_group_id",
            x_llama_stack_provider_data="X-LlamaStack-ProviderData",
        )
        assert tool_group is None

    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        response = await async_client.tool_groups.with_raw_response.unregister(
            tool_group_id="tool_group_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool_group = await response.parse()
        assert tool_group is None

    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncLlamaStackClient) -> None:
        async with async_client.tool_groups.with_streaming_response.unregister(
            tool_group_id="tool_group_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool_group = await response.parse()
            assert tool_group is None

        assert cast(Any, response.is_closed) is True
