#!/usr/bin/python3
'''
Minimum Operations: You can only use to keys to reproduce a certain letter
n times
'''


def minOperations(n):
    if n <= 1:
        return 0  # No operations needed for n <= 1

    dp = [0] * (n + 1)  # Initialize the dp array with zeros

    for i in range(2, n + 1):
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                dp[i] = dp[j] + i // j

    return dp[n]
