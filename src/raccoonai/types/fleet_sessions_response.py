# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FleetSessionsResponse", "Meta", "Session"]


class Meta(BaseModel):
    current_page: int = FieldInfo(alias="currentPage")
    """The current page number."""

    total_pages: int = FieldInfo(alias="totalPages")
    """Total number of pages available."""

    total_records: int = FieldInfo(alias="totalRecords")
    """Total number of records across all pages."""


class Session(BaseModel):
    execution_time: int = FieldInfo(alias="executionTime")
    """Time taken for the session execution (in milliseconds)."""

    execution_type: Literal["run", "extract", "fleet"] = FieldInfo(alias="executionType")
    """The type of execution performed (e.g., 'run', 'extract')."""

    inputs: object
    """Input parameters used for the session."""

    output: List[object]
    """Output generated by the session."""

    raccoon_passcode: str = FieldInfo(alias="raccoonPasscode")
    """Passcode associated with the user."""

    session_id: str = FieldInfo(alias="sessionId")
    """Unique identifier for the session."""

    status: Literal["success", "failure", "running"]
    """Current status of the session."""

    task_id: str = FieldInfo(alias="taskId")
    """Unique identifier for the associated task."""

    timestamp: int
    """Unix timestamp (in milliseconds) indicating when the session was created."""


class FleetSessionsResponse(BaseModel):
    meta: Meta
    """Metadata about the session list."""

    sessions: List[Session]
    """List of sessions."""
