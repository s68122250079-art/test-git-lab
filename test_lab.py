def std_dev(values):
    if not values:
        return None
    m = sum(values) / len(values)
    return (sum((v - m) ** 2 for v in values) / len(values)) ** 0.5
def test_std_dev():
    assert std_dev([2, 4, 4, 4, 5, 5, 7, 9]) == 2.0
    assert std_dev([]) is None