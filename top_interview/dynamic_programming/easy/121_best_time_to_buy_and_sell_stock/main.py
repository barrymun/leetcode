from typing import List


def max_profit(prices: List[int]) -> int:
    res = 0
    if len(prices) == 0:
        return res
    buy = prices[0]  # buy low
    sell = prices[0]  # sell high
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]  # new low buy price
            sell = prices[i]  # reset sell price, as you cannot sell before you buy
        elif prices[i] > sell:
            sell = prices[i]  # new higher sell price
            if res < sell - buy:  # only update if a new maximum is achieved
                res = sell - buy
    return res


if __name__ == '__main__':
    print(max_profit(prices=[7, 1, 5, 3, 6, 4]))
    print(max_profit(prices=[7, 6, 4, 3, 1]))
    print(max_profit(prices=[1, 2]))
