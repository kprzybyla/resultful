import pytest

from hypothesis import (
    given,
    strategies as st,
)

from resultful import (
    unsafe,
    success,
    failure,
    unwrap_failure,
    Result,
    NoResult,
)

from .conftest import (
    st_exceptions,
    unreachable,
)


@given(error=st_exceptions())
def test_special_methods(error: BaseException) -> None:
    result = failure(error)

    assert bool(result) is False
    assert repr(result) == f"resultful.Failure({error!r})"


@given(error=st_exceptions())
def test_unsafe(error: BaseException) -> None:
    with pytest.raises(BaseException) as exception:
        unsafe(failure(error))

    assert exception.value is error


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
def test_result_if_condition(error: BaseException) -> None:
    def compute() -> Result[int, BaseException]:
        return failure(error)

    result = compute()

    if not result:
        assert result.error is error
    else:
        unreachable()

    if result.is_failure:
        assert result.error is error
    else:
        unreachable()

    if result.is_success:
        unreachable()
    else:
        assert result.error is error


@given(error=st_exceptions())
def test_result_if_condition_walrus_operator(error: BaseException) -> None:
    def compute() -> Result[int, BaseException]:
        return failure(error)

    if not (result := compute()):
        assert result.error is error
    else:
        unreachable()

    if (result := compute()).is_failure:
        assert result.error is error
    else:
        unreachable()

    if (result := compute()).is_success:
        unreachable()
    else:
        assert result.error is error
