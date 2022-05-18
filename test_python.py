import math
from my_module import filter_int_only,square

def test_filter():
    l1 = [2, -5, 3.56, 'text']
    l2 = list(filter(filter_int_only, l1))
    assert set(l2).issubset(set(l1))
    assert len(l2) <= len(l1)
    assert isinstance(-5, int)

def test_map():
    numbers=[4,56.3,3,9,1]
    squared=list(map(square, numbers))
    assert numbers[0]**2==squared[0]
    assert len(numbers) == len(squared)

def test_sorted():
    smpl1 = "text sample"
    smpl2 = sorted(smpl1, reverse=True)
    assert len(smpl1) == len(smpl2)
    assert type(smpl2) == list

def test_pi():
    assert math.pi == 3.141592653589793

def test_sqrt():
    assert math.sqrt(9) == 3

def test_pow():
    assert math.pow(2, 3) == 8

def test_hypot():
    assert math.sqrt(2 * 2 + 3 * 3) == 3.605551275463989


