# Time: O(n), Space: O(n)
def stair(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[n]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print stair(n)