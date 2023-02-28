class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort() #sort it simply
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1]) #last 3 or first*second
        