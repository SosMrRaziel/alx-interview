#!/usr/bin/python3
""" Making Change """

def makeChange(coins, total) -> int:
    # Initialize an array to store minimum coins needed for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for value 0

    for value in range(1, total + 1):
        for coin in coins:
            if coin <= value:
                dp[value] = min(dp[value], dp[value - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
