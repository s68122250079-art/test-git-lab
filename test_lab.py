def std_dev(values):
    if not values:
        return None
    m = sum(values) / len(values)
    return (sum((v - m) ** 2 for v in values) / len(values)) ** 0.5

def test_std_dev():
    assert std_dev([2, 4, 4, 4, 5, 5, 7, 9]) == 2.0
    assert std_dev([]) is None

def value_range(values):
    if not values:
        return None
    return max(values) - min(values)

def test_value_range():
    assert value_range([3, 9, 4]) == 6
    assert value_range([5]) == 0
    assert value_range([-2, 3]) == 5
    assert value_range([]) is None