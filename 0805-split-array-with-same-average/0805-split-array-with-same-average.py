class Solution:
    def solve(self, nums, i, n, sums, count, dp):
        if count == 0 and sums == 0:
            return True
        if i == n or count < 0 or sums < 0:
            return False
        if dp[i][count][sums] != -1:
            return dp[i][count][sums]
        dp[i][count][sums] = self.solve(nums, i+1, n, sums-nums[i], count-1, dp) or self.solve(nums, i+1, n, sums, count, dp)
        return dp[i][count][sums]

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n, summ = len(nums), sum(nums)
        for i in range(1, n):
            if summ * i % n == 0:
                tsum = summ * i // n
                dp = [[[-1 for _ in range(tsum+1)] for _ in range(i+1)] for _ in range(n+1)]
                if self.solve(nums, 0, n, tsum, i, dp):
                    return True
        return False
