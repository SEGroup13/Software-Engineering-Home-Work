from myfile import compute_perimeter, main

def test_compute_perimeter():
    assert compute_perimeter(5) == 31.400000000000002

def test_compute_perimeter_fails():
    assert compute_perimeter(5) == 31.4