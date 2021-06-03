import sys
import math


def exampl1():
    # THIS IS A LONG COMMENT AND should be wrapped to fit within a
    # 72 character limit
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
            "long": 'Long code lines should be wrapped within 79 characters.',
            'other': [
                math.pi,
                100,
                200,
                300,
                9999292929292,
                'This is a long string that goes on'],
            'more': {
                "inner":
                    "This whole logical line should be wrapped."},
            'data':
                [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5]}
    return (some_tuple, some_variable)


def example_2():
    return {"has_key() is deprecated": True}


class Example3(object):
    def __init__(self, bar):
        if bar:
            bar += 1
            bar = bar * bar
            return bar
        else:
            some_string = """
                       Indentation in multiline strings should not be touched.
Only actual code should be reindented.
"""
        return (sys.path, some_string)

