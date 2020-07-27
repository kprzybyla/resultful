from hypothesis import given
from hypothesis import strategies as st

from resultful import success, failure, unwrap_success, NoResult

from .conftest import st_exceptions


@given(value=st.integers())
def test_special_methods(value: int) -> None:
    result = success(value)

    assert bool(result) is True
    assert repr(result) == f"resultful.Success({value!r})"


@given(value=st.integers())
def test_equality(value: int) -> None:
    assert success(value) == success(value)


@given(error=st_exceptions())
def test_inequality_with_failure(error: BaseException) -> None:
    assert success(error) != failure(error)


@given(value=st.integers())
def test_unwrap_success_from_success(value: int) -> None:
    result = unwrap_success(success(value))

    assert result is value


@given(error=st_exceptions())
def test_unwrap_success_from_failure(error: BaseException) -> None:
    result = unwrap_success(failure(error))

    assert result is NoResult


@given(value=st.integers())
def test_value(value: int) -> None:
    result = success(value)

    assert result
    assert result.value is value


@given(value=st.integers())
def test_value_wrapped_in_success(value: int) -> None:
    result = success(success(value))

    assert result
    assert result.value is value


@given(error=st_exceptions())
def test_error_wrapped_in_failure(error: Exception) -> None:
    result = success(failure(error))

    assert result is NoResult


@given(value=st.integers())
def test_walrus_operator(value: int) -> None:
    if result := success(value):
        assert result.value is value
    else:
        assert False
