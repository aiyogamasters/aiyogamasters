import pytest
from projects.simple_example import greet

def test_greet_returns_expected_string():
    assert greet('Test') == 'Namaste, Test!'
