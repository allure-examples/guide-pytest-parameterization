import pytest


def test_sum():
    assert 1 + 2 == 3

def test_sum_loop():
    data = [
        [1, 2, 3],
        [-1, 1, 0],
        [0, 0, 0]
    ]
    for x, y, ttl in data:
        assert x + y == ttl

data = [
    [1, 2, 3],
    [-1, 1, 0],
    [0, 0, 0]
]

def prepare_test_data(param):
    return data[param]

@pytest.mark.parametrize("x,y,ttl", data)
def test_sum_parameterized(x, y, ttl):
    assert x + y == ttl

@pytest.fixture(params=[0, 1, 2])
def sum_arguments(request):
    yield prepare_test_data(request.param)

def test_sum_simple(sum_arguments):
    x, y, ttl = sum_arguments
    assert x + y == ttl

def test_sum_keyword(sum_arguments):
    x, y, ttl = sum_arguments
    assert sum((x, y)) == ttl