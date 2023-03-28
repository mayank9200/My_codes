class Solution:
    #https://www.youtube.com/watch?v=D8m8eWP8w4E
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        incr=1
        decr=1
        for i in range(1,n):
            if nums[i]-nums[i-1]>0:
                incr=decr+1
            elif nums[i]-nums[i-1]<0:
                decr=incr+1
        return max(incr,decr)        