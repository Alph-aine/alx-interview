#!/usr/bin/python3
'''Making Change'''


def makeChange(coins, total):
    '''finds the minimum number of coins needed to get a total'''
    if total <= 0:
        return 0

    temp = total
    n = len(coins)
    coins_count = 0
    index = 0

    sorted_coins = sorted(coins, reverse=True)

    while temp > 0:
        if index >= n:
            return -1
        if temp - sorted_coins[index] >= 0:
            temp -= sorted_coins[index]
            coins_count += 1
        else:
            index += 1

    return coins_count
