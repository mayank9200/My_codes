class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        ladder=nums[0]
        for i in range(n):
            if i>ladder:
                return False
            ladder=max(ladder,nums[i]+i)
        return True    
            
        