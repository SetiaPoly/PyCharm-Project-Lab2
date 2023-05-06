import Ex2 as temp

def test_find_min_max():
    min_max = temp.find_min_max()

    assert (min_max == 4)

def test_calc_average():
    calc_average = temp.calc_average()

    assert (calc_average == 3)

def test_calc_median_temperature():
    median = temp.calc_median_temperature()

    assert (median == 5,6)