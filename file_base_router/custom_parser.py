import argparse
import functools


class Parser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(description="File Based Router")

    def use_parser(self):
        """
        return function for creating adding argument to parser

        """

        def register_argument(parser_func):
            @functools.wraps(parser_func)
            def parser_func_wrapper(*args, **kwargs):
                parser_func(*args, **kwargs)

            return parser_func_wrapper

        return register_argument
