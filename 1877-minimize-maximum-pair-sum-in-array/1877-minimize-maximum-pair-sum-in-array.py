class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)-1
        maxx=float('-inf')
        print(nums)
        for i in range(n//2+1):
            maxx=max(maxx,nums[i]+nums[n-i])
            print(nums[i]+nums[n-i])
        return maxx    
        