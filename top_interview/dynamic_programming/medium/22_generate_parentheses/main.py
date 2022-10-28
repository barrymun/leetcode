from typing import List


def generate_parenthesis(n: int) -> List[str]:
    res = []
    if n < 1 or n > 8:
        return res
    for i in range(0, n):
        pass
    return res


if __name__ == '__main__':
    print(generate_parenthesis(n=0))
    print(generate_parenthesis(n=1))
