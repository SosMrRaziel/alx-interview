#!/usr/bin/python3
""" Making Change """
from typing import List


def makeChange(coins: list, total: int) -> int:
    """ Initialize an array to store minimum coins needed for each value """
    sorted_coins = sorted(coins, reverse=True)
    dp = 0
    for coin in sorted_coins:
        if total == 0:
            break
        dp += total // coin
        total = total % coin
    if total == 0:
        return dp
    return -1
