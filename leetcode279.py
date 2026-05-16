##leetcode 279: Perfect Squares
class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def solve(x):
            if x == 0:
                return 0
            if x in memo:
                return memo[x]

            ans = float('inf')
            i = 1
            while i * i <= x:
                ans = min(ans, 1 + solve(x - i * i))
                i += 1

            memo[x] = ans
            return ans

        return solve(n)
