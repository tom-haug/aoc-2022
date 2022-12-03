from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar("T")


@dataclass
class FileResult(Generic[T]):
    file_path: str
    expected_result: Optional[T]

    def __init__(self, file_path: str, expected_result: Optional[T]):
        self.file_path = file_path
        self.expected_result = expected_result
