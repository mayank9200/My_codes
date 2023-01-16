class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        actual_sum=sum(nums)
        expected_sum=((n+1)*(n))//2
        return expected_sum-actual_sum
        