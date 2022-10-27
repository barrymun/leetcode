def climb_stairs(n: int) -> int:
    """
    utilising memoization
    :param n:
    :return:
    """
    res = 1  # will take at least 1 step
    one, two = 1, 1  # both start from the first step
    for i in range(0, n - 1):
        res = one + two
        two = one
        one = res
    return res


if __name__ == '__main__':
    for x in range(1, 6):
        print(f'n={x}, res={climb_stairs(n=x)}')
