import pytest


def test_success():
    """this 1 ok"""
    assert 1


def test_fail():
    """this 1 bad"""
    assert 0


def test_skip():
    """skip dat"""
    pytest.skip('sorry')


def test_broken():
    raise Exception('oops')
