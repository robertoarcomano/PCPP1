from common import title
import traceback


class MyClassException(BaseException):
    pass


def test_implicit_context():
    try:
        a = 0 / 0
    except ZeroDivisionError as z:
        try:
            import xxx
        except BaseException as b:
            return b


def test_explicit_cause():
    try:
        a = 0 / 0
    except ZeroDivisionError as z:
        try:
            raise MyClassException("MyClassException") from z
        except BaseException as b:
            return b


implicit = test_implicit_context()
title("test_implicit_context()", implicit, implicit.__context__, implicit.__traceback__,
      traceback.format_tb(implicit.__traceback__), traceback.print_tb(implicit.__traceback__))
explicit = test_explicit_cause()
title("test_explicit_cause()", explicit, explicit.__cause__, explicit.__traceback__,
      traceback.format_tb(explicit.__traceback__), traceback.print_tb(explicit.__traceback__))
