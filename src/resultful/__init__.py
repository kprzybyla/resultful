__all__ = (
    "AlwaysSuccess",
    "AlwaysFailure",
    "Result",
    "ResultType",
    "NoResultType",
    "unsafe",
    "success",
    "failure",
    "unwrap_success",
    "unwrap_failure",
    "NoResult",
)

# Annotations

from .result import (
    AlwaysSuccess,
    AlwaysFailure,
    Result,
)

# Types

from .result import (
    ResultType,
    NoResultType,
)

# Concretes

from .result import (
    unsafe,
    success,
    failure,
    unwrap_success,
    unwrap_failure,
    NoResult,
)
