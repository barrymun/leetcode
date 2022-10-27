from typing import List


def generate(num_rows: int) -> List[List[int]]:
    """
    :param num_rows: 1 <= num_rows <= 30
    :return:
    """
    if num_rows < 1 or num_rows > 30:
        return None
    res = [[1]]
    for i in range(1, num_rows):
        arr = []
        for j in range(0, len(res[i - 1]) - 1):
            arr.append(res[i - 1][j] + res[i - 1][j + 1])
        res.append([1, *arr, 1])
    return res


if __name__ == '__main__':
    print(generate(num_rows=0))
    print(generate(num_rows=31))
    print(generate(num_rows=1))
    print(generate(num_rows=2))
    print(generate(num_rows=3))
    print(generate(num_rows=4))
    print(generate(num_rows=5))
    print(generate(num_rows=6))
