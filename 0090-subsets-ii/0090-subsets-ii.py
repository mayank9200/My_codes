class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        ans=[]
        s=set()
        for i in range(0,pow(2,n)):
            temp=[]
            c=0
            j=i
            while j>0:
                if j&1==1:
                    temp.append(nums[c])          
                c+=1
                j=j>>1
            if tuple(temp) not in s:    
                ans.append(temp) 
                s.add(tuple(temp))        
        return ans
        