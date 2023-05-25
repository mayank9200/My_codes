class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        d1={}
        d2={}
        l1=[]
        l2=[]
        n=len(nums)
        for i in range(n):
            d1[nums[i]]=d1.get(nums[i],0)+1
            l1.append(len(d1))
        for i in range(n-1,-1,-1):
            d2[nums[i]]=d2.get(nums[i],0)+1
            l2.append(len(d2))
        l2=l2[::-1]
        
        ans=[]
        for i in range(n-1):
            ans.append(l1[i]-l2[i+1])
        ans.append(l1[n-1])
        return ans    

            