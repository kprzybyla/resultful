from hypothesis import given
from hypothesis import strategies as st

from resultful import success, failure, unwrap_failure, NoResult

from .conftest import st_exceptions


@given(error=st_exceptions())
def test_special_methods(error: BaseException) -> None:
    result = failure(error)

    assert bool(result) is False
    assert repr(result) == f"resultful.Failure({error!r})"


@given(error=st_exceptions())
def test_equality(error: BaseException) -> None:
    assert failure(error) == failure(error)


@given(error=st_exceptions())
def test_inequality_with_success(error: BaseException) -> None:
    assert failure(error) != success(error)


@given(error=st_exceptions())
def test_unwrap_failure_from_failure(error: BaseException) -> None:
    result = unwrap_failure(failure(error))

    assert result is error


@given(value=st.integers())
def test_unwrap_failure_from_success(value: int) -> None:
    result = unwrap_failure(success(value))

    assert result is NoResult


@given(error=st_exceptions())
def test_error(error: BaseException) -> None:
    result = failure(error)

    assert not result
    assert result.error is error


@given(error=st_exceptions())
def test_error_wrapped_in_failure(error: BaseException) -> None:
    result = failure(failure(error))

    assert not result
    assert result.error is error


@given(value=st.integers())
def test_error_wrapped_in_success(value: int) -> None:
    result = failure(success(value))

    assert result is NoResult


@given(error=st_exceptions())
def test_walrus_operator(error: BaseException) -> None:
    if not (result := failure(error)):
        assert result.error is error
    else:
        assert False
