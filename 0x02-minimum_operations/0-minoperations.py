#!/usr/bin/python3
'''
Minimum Operations: You can only use to keys to reproduce a certain letter
n times
'''


def minOperations(n):
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Initialize dp[i] with the worst-case scenario

        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]
