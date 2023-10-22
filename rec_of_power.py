def rec_of_power(base, exp):
    assert int(exp) == exp, 'Edge case'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / base * rec_of_power(base, exp + 1)
    return base * rec_of_power(base, exp - 1)
