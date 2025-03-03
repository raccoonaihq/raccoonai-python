# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from raccoonai import RaccoonAI, AsyncRaccoonAI
from tests.utils import assert_matches_type
from raccoonai.types import (
    FleetLogsResponse,
    FleetCreateResponse,
    FleetStatusResponse,
    FleetSessionsResponse,
    FleetTerminateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFleet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: RaccoonAI) -> None:
        fleet = client.fleet.create()
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: RaccoonAI) -> None:
        fleet = client.fleet.create(
            advanced={
                "block_ads": True,
                "extension_ids": ["df2399ea-a938-438f-9d4b-ef3bc95cf8af"],
                "proxy": {
                    "city": "sanfrancisco",
                    "country": "us",
                    "enable": True,
                    "state": "ca",
                    "zip": 94102,
                },
                "solve_captchas": True,
            },
            browser_type="chromium",
            headless=True,
            raccoon_passcode="<end-user-raccoon-passcode>",
            session_timeout=600,
            settings={
                "locales": ["en-US", "fr-FR"],
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "viewport": {
                    "height": 720,
                    "width": 1280,
                },
            },
            url="https://www.google.com",
        )
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: RaccoonAI) -> None:
        response = client.fleet.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: RaccoonAI) -> None:
        with client.fleet.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetCreateResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_logs(self, client: RaccoonAI) -> None:
        fleet = client.fleet.logs(
            "session_id",
        )
        assert_matches_type(FleetLogsResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_logs(self, client: RaccoonAI) -> None:
        response = client.fleet.with_raw_response.logs(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetLogsResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_logs(self, client: RaccoonAI) -> None:
        with client.fleet.with_streaming_response.logs(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetLogsResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_logs(self, client: RaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.fleet.with_raw_response.logs(
                "",
            )

    @parametrize
    def test_method_sessions(self, client: RaccoonAI) -> None:
        fleet = client.fleet.sessions()
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    def test_method_sessions_with_all_params(self, client: RaccoonAI) -> None:
        fleet = client.fleet.sessions(
            end_time=1678972800000,
            execution_type=["run"],
            limit=15,
            page=2,
            raccoon_passcode="code456",
            session_id="session_456",
            sort_by="timestamp",
            sort_order="ascend",
            start_time=1678886400000,
            task_id="task_123",
        )
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_sessions(self, client: RaccoonAI) -> None:
        response = client.fleet.with_raw_response.sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_sessions(self, client: RaccoonAI) -> None:
        with client.fleet.with_streaming_response.sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_status(self, client: RaccoonAI) -> None:
        fleet = client.fleet.status(
            "session_id",
        )
        assert_matches_type(FleetStatusResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_status(self, client: RaccoonAI) -> None:
        response = client.fleet.with_raw_response.status(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetStatusResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_status(self, client: RaccoonAI) -> None:
        with client.fleet.with_streaming_response.status(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetStatusResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_status(self, client: RaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.fleet.with_raw_response.status(
                "",
            )

    @parametrize
    def test_method_terminate(self, client: RaccoonAI) -> None:
        fleet = client.fleet.terminate(
            "session_id",
        )
        assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

    @parametrize
    def test_raw_response_terminate(self, client: RaccoonAI) -> None:
        response = client.fleet.with_raw_response.terminate(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = response.parse()
        assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

    @parametrize
    def test_streaming_response_terminate(self, client: RaccoonAI) -> None:
        with client.fleet.with_streaming_response.terminate(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = response.parse()
            assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_terminate(self, client: RaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.fleet.with_raw_response.terminate(
                "",
            )


class TestAsyncFleet:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.create()
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.create(
            advanced={
                "block_ads": True,
                "extension_ids": ["df2399ea-a938-438f-9d4b-ef3bc95cf8af"],
                "proxy": {
                    "city": "sanfrancisco",
                    "country": "us",
                    "enable": True,
                    "state": "ca",
                    "zip": 94102,
                },
                "solve_captchas": True,
            },
            browser_type="chromium",
            headless=True,
            raccoon_passcode="<end-user-raccoon-passcode>",
            session_timeout=600,
            settings={
                "locales": ["en-US", "fr-FR"],
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "viewport": {
                    "height": 720,
                    "width": 1280,
                },
            },
            url="https://www.google.com",
        )
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncRaccoonAI) -> None:
        response = await async_client.fleet.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetCreateResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncRaccoonAI) -> None:
        async with async_client.fleet.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetCreateResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_logs(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.logs(
            "session_id",
        )
        assert_matches_type(FleetLogsResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncRaccoonAI) -> None:
        response = await async_client.fleet.with_raw_response.logs(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetLogsResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncRaccoonAI) -> None:
        async with async_client.fleet.with_streaming_response.logs(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetLogsResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_logs(self, async_client: AsyncRaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.fleet.with_raw_response.logs(
                "",
            )

    @parametrize
    async def test_method_sessions(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.sessions()
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    async def test_method_sessions_with_all_params(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.sessions(
            end_time=1678972800000,
            execution_type=["run"],
            limit=15,
            page=2,
            raccoon_passcode="code456",
            session_id="session_456",
            sort_by="timestamp",
            sort_order="ascend",
            start_time=1678886400000,
            task_id="task_123",
        )
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_sessions(self, async_client: AsyncRaccoonAI) -> None:
        response = await async_client.fleet.with_raw_response.sessions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_sessions(self, async_client: AsyncRaccoonAI) -> None:
        async with async_client.fleet.with_streaming_response.sessions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetSessionsResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_status(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.status(
            "session_id",
        )
        assert_matches_type(FleetStatusResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_status(self, async_client: AsyncRaccoonAI) -> None:
        response = await async_client.fleet.with_raw_response.status(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetStatusResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncRaccoonAI) -> None:
        async with async_client.fleet.with_streaming_response.status(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetStatusResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_status(self, async_client: AsyncRaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.fleet.with_raw_response.status(
                "",
            )

    @parametrize
    async def test_method_terminate(self, async_client: AsyncRaccoonAI) -> None:
        fleet = await async_client.fleet.terminate(
            "session_id",
        )
        assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

    @parametrize
    async def test_raw_response_terminate(self, async_client: AsyncRaccoonAI) -> None:
        response = await async_client.fleet.with_raw_response.terminate(
            "session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fleet = await response.parse()
        assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

    @parametrize
    async def test_streaming_response_terminate(self, async_client: AsyncRaccoonAI) -> None:
        async with async_client.fleet.with_streaming_response.terminate(
            "session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fleet = await response.parse()
            assert_matches_type(FleetTerminateResponse, fleet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_terminate(self, async_client: AsyncRaccoonAI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.fleet.with_raw_response.terminate(
                "",
            )
