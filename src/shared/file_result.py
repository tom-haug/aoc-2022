from typing import Any, Generic, Optional, TypeVar


T = TypeVar("T")


class FileResult(Generic[T]):
    file_path: str
    expected_result: Optional[T]
    extra_params: dict[str, Any]

    def __init__(
        self,
        file_path: str,
        expected_result: Optional[T],
        extra_params: dict[str, Any] = {},
    ):
        self.file_path = file_path
        self.expected_result = expected_result
        self.extra_params = extra_params
