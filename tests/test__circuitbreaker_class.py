
import pytest

from circuitbreaker_toolkit.breaker import (
    breaker_factory,
    State,
    CircuitBreaker,
)



def test__default():
    breaker = breaker_factory()


def test__basic():

    breaker = breaker_factory()
    breaker.start()
    breaker.no_exception()
    breaker.end()


