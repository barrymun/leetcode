def climb_stairs(n: int) -> int:
    res = 1  # will take at least 1 step
    one, two = 1, 1  # both start from the first step
    for i in range(0, n - 1):
        res = one + two
        two = one
        one = res
    return res


if __name__ == '__main__':
    for n in range(1, 6):
        print(f'n={n}, res={climb_stairs(n=n)}')
