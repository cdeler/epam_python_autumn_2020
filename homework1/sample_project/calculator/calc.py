def check_power_of_2(a: int) -> bool:
    return not (bool(a & (a - 1)))
