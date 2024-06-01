"""
Function decorators

"""
import time as Time
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


def measure_runtime(func):
    @functools.wraps(func)
    def runtime_wrapper(*arg, **kwarg):
        start = Time.perf_counter()
        value = func(*arg, **kwarg)
        stop = Time.perf_counter()
        run_time = stop - start
        print(f"{func.__name__} took {run_time:.4f} seconds")
        return value
    return runtime_wrapper


def debug(callback):
    """
        Logs callback function return value and arg

    """
    @functools.wraps(callback)
    def debug_wrapper(*arg, **kwargs):
        argument1 = [repr(x)for x in arg]
        kwarg = [f"{x}={y}" for x,y in kwargs.items()]
        value = callback(*arg,**kwargs)
        argument1.extend(kwarg)
        logs = ", ".join(argument1)
        print(f"calling {callback.__name__}({logs})")
        print(f"{callback.__name__}() returned {repr(value)}")
        return value
    return  debug_wrapper


























