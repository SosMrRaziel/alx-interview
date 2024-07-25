#!/usr/bin/python3
""" Making Change """
from typing import List


def makeChange(coins: list, total: int) -> int:
    """ Initialize an array to store minimum coins needed for each value """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for 0 total

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Check if the total can be formed
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
