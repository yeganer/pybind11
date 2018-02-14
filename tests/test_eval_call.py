# This file is called from 'test_eval.py'

if 'call_test2' in locals():
    call_test2(y)  # noqa: F821 undefined name


def local_function():
    call_test2(y)


local_function()
