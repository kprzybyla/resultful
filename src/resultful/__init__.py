__all__ = [
    "Result",
    "ResultType",
    "NoResultType",
    "success",
    "failure",
    "unwrap_success",
    "unwrap_failure",
    "NoResult",
]

# Annotations

from .result import Result

# Types

from .result import (
    ResultType,
    NoResultType,
)

# Concretes

from .result import (
    success,
    failure,
    unwrap_success,
    unwrap_failure,
    NoResult,
)
