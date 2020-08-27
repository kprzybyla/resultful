from typing import (
    Type,
    TypeVar,
    Sequence,
    NoReturn,
)

from hypothesis import strategies as st

Ex = TypeVar("Ex")

EXCEPTIONS: Sequence[Type[BaseException]] = [
    BaseException,
    SystemExit,
    KeyboardInterrupt,
    GeneratorExit,
    Exception,
    StopIteration,
    StopAsyncIteration,
    ArithmeticError,
    FloatingPointError,
    OverflowError,
    ZeroDivisionError,
    AssertionError,
    AttributeError,
    BufferError,
    EOFError,
    ImportError,
    ModuleNotFoundError,
    LookupError,
    IndexError,
    KeyError,
    MemoryError,
    NameError,
    UnboundLocalError,
    OSError,
    BlockingIOError,
    ChildProcessError,
    ConnectionError,
    BrokenPipeError,
    ConnectionAbortedError,
    ConnectionRefusedError,
    ConnectionResetError,
    FileExistsError,
    FileNotFoundError,
    InterruptedError,
    IsADirectoryError,
    NotADirectoryError,
    PermissionError,
    ProcessLookupError,
    TimeoutError,
    ReferenceError,
    RuntimeError,
    NotImplementedError,
    RecursionError,
    SyntaxError,
    IndentationError,
    TabError,
    SystemError,
    TypeError,
    ValueError,
    UnicodeError,
    Warning,
    DeprecationWarning,
    PendingDeprecationWarning,
    RuntimeWarning,
    SyntaxWarning,
    UserWarning,
    FutureWarning,
    ImportWarning,
    UnicodeWarning,
    BytesWarning,
    ResourceWarning,
]


def st_exceptions() -> st.SearchStrategy[BaseException]:
    return st.sampled_from(EXCEPTIONS).map(lambda exception: exception())


def unreachable() -> NoReturn:
    assert False
