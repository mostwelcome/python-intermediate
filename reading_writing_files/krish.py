"""Writes Random Function."""


def foo(num: int) -> str:
    """Random function.

    Parameters
    ----------
        num: int
            Number to check +ve or -ve.

    Returns
    -------
        str
            Positive or negative.
    """
    if num > 0:
        return '+ve'
    return '-ve'


print(foo(5))
