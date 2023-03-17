class Solution:
    def jump(self, nums: List[int]) -> int:
        if nums[0]==0 or len(nums)==1:
            return 0
        #https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1
        #simple ladder and stair formula, as soon as we change ladder ie. stairs get over we increment jump
        ladder=nums[0]
        stairs=nums[0]
        n=len(nums)
        jumps=1
        for i in range(1,n):
            if i==n-1:
                return jumps #reached last pos
            ladder=max(ladder,nums[i]+i) #max pos till we can go
            stairs=stairs-1
            if stairs==0: #have to change ladder now
                stairs=ladder-i #remaining steps on that changed ladder
                jumps+=1 #did a jump
        return jumps        
        