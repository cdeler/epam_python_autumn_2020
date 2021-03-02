def check_power_of_2(a: int) -> bool:
    return a & (a - 1) == 0 and a != 0
