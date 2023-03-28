class Solution:
    #https://www.youtube.com/watch?v=D8m8eWP8w4E
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n=len(nums)
        incr=1 #till that point ending at increasing subsequence length
        decr=1 #till that point ending at decreasing subsequence length
        for i in range(1,n):
            if nums[i]-nums[i-1]>0: #if increasing
                incr=decr+1 #at 1 to decreasing and increasing remain as it is
            elif nums[i]-nums[i-1]<0: #if decreasing
                decr=incr+1 #at 1 to increasing and decreasing remain as it is
        return max(incr,decr)   #max of increasing and decreasing is the ans   