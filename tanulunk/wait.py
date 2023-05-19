"""Waiter wrapper function for class methods"""
import time


def wait_delay(timeout):
    """Waits delay after function call"""

    def decorate(function):
        def wrapper(*args, **kwargs):
            output = function(*args, **kwargs)
            time.sleep(timeout)
            return output

        return wrapper

    return decorate
