import pytest
import time
from pe5 import multi_table

@pytest.fixture(autouse=True)
def timer(request):
    start_time = time.time()
    yield
    duration = time.time() - start_time
    print(f"\nTest duration is {duration:.6f} seconds")

@pytest.mark.basic
def basic_1():
    assert multi_table[3][4] == 12

@pytest.mark.basic
def basic_2():
    assert multi_table[5][5] == 'X'

@pytest.mark.xfail
def test_expected_fail():
    assert multi_table[2][11] == 100

def test_index_error():
    with pytest.raises(IndexError):
        value = multi_table[13][6]

@pytest.mark.parametrize("i, j, expected", [
    (2, 3, 6),
    (6, 6, multi_table[6][6]),
    (8, 4, 32),
    (11, 10, 110),
])

def test_parametrized(i, j, expected):
    assert multi_table[i][j] == expected