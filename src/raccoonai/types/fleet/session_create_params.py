# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, TypedDict

__all__ = ["SessionCreateParams", "Advanced", "AdvancedProxy", "Settings"]


class SessionCreateParams(TypedDict, total=False):
    advanced: Optional[Advanced]
    """
    Advanced configuration options for the session, such as ad-blocking and CAPTCHA
    solving.
    """

    browser_type: Optional[Literal["chromium", "firefox", "webkit"]]
    """The type of browser to use.

    Supported values include 'chromium', 'firefox', and 'webkit'.
    """

    headless: Optional[bool]
    """Whether to run the browser in headless mode."""

    raccoon_passcode: Optional[str]
    """
    The raccoon passcode associated with the end user on behalf of which the call is
    being made if any.
    """

    session_timeout: Optional[int]
    """The timeout for the browser session in seconds."""

    settings: Optional[Settings]
    """
    Configuration settings for the browser, such as viewport size and User-Agent
    string.
    """

    url: Optional[str]
    """The entrypoint url for the session."""


class AdvancedProxy(TypedDict, total=False):
    city: Optional[str]
    """Target city."""

    country: Optional[str]
    """Target country (2-letter ISO code)."""

    enable: bool
    """Whether to use a proxy for the browser session."""

    state: Optional[str]
    """Target state (2-letter code)."""

    zip: Optional[int]
    """Target postal code."""


class Advanced(TypedDict, total=False):
    block_ads: Optional[bool]
    """Whether to block advertisements during the browser session."""

    extension_ids: Optional[Iterable[object]]
    """list of extension ids"""

    proxy: Optional[AdvancedProxy]
    """Proxy details for the browser session."""

    solve_captchas: Optional[bool]
    """Whether to attempt automatic CAPTCHA solving."""


class Settings(TypedDict, total=False):
    locales: Optional[List[str]]
    """A list of locales or languages to use for the browser session.

    These determine language preferences.
    """

    user_agent: Optional[str]
    """The User-Agent string to use for the browser.

    Defaults to internal auto user-agent rotation mechanism.
    """

    viewport: Optional[Dict[str, int]]
    """The viewport size (screen dimensions) for the browser in pixels."""
