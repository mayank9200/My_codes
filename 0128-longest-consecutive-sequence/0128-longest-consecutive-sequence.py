class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        if len(nums)==0:
            return 0
        maxx=1
        for i in nums:
            s.add(i)
        for i in nums:
            if i-1 not in s:
                temp=i
                count=0
                while temp in s:
                    count+=1
                    temp+=1
                maxx=max(maxx,count)    
        return maxx       
        