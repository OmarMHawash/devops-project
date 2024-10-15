"""Pytest fixtures for unit tests"""
import pytest

@pytest.fixture
def my_fixture():
    """My fixture"""
    yield "some_value"
