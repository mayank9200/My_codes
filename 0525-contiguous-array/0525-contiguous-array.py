class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d={}
        maxx=0
        pre=0
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        for i in range(len(nums)):
            pre=pre+nums[i]
            if pre in d:
                maxx=max(maxx,i-d[pre])
            if pre==0:
                maxx=max(maxx,i+1)
            if pre not in d:
                d[pre]=i
        return maxx        
                
        