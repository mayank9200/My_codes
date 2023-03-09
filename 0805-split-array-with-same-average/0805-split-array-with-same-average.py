class Solution:
    def solve(self, nums, i, n, sums, count, dp): #to find if there a sum exist with i numbers
        if count == 0 and sums == 0:
            return True
        if i == n or count < 0 or sums < 0:
            return False
        if dp[i][count][sums] != -1:
            return dp[i][count][sums]
        dp[i][count][sums] = self.solve(nums, i+1, n, sums-nums[i], count-1, dp) or self.solve(nums, i+1, n, sums, count, dp)
        return dp[i][count][sums]

    def splitArraySameAverage(self, nums: List[int]) -> bool:
        #https://www.youtube.com/watch?v=VwylCVAVdmo
        # s1//n1==s2//n1
        # s1+s2=summ
        # n1+n2=n
        # find value of s1 ie s1=(summ*n1)//n
        # now for all possible s1 and corresponding n1 check if this combination is possible
        n, summ = len(nums), sum(nums)
        for i in range(1, n):
            if summ * i % n == 0: #if possible sum is integer then only proceed
                tsum = summ * i // n
                dp = [[[-1 for _ in range(tsum+1)] for _ in range(i+1)] for _ in range(n+1)] #for memorization since three variables are changing,hence a 3d dp
                if self.solve(nums, 0, n, tsum, i, dp):
                    return True
        return False
