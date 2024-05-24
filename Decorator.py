"""
Function decorators

"""
import functools
def do_twice(func):
    """
        Executes callback function twice

        USAGE:
    >>> @do_twice
    >>> def console():
    >>>     print("Hello World")
        Hello World

    """
    @functools.wraps(func)
    def do_wrapper(*arg,**kwarg):
        """
         do_wrapper calls callback function twice.

        """
        func(*arg,**kwarg)
        return func(*arg,**kwarg)
    return do_wrapper
