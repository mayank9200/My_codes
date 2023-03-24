class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n=len(nums)
        lnb=[-1 for i in range(n)]
        rnb=[float('inf') for i in range(n)]
        lnb[0]=nums[0]
        rnb[n-1]=nums[n-1]
        count=0
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                lnb[i]=lnb[i-1]
            else:
                lnb[i]=nums[i-1]
        for i in range(n-2,-1,-1):
            if nums[i]==nums[i+1]:
                rnb[i]=rnb[i+1]
            else:
                rnb[i]=nums[i+1]
        for i in range(1,n-1):
            if nums[i]!=nums[i-1]:
                if nums[i]>lnb[i] and nums[i]>rnb[i]:
                    #print(nums[i])
                    count+=1
                elif nums[i]<lnb[i] and nums[i]<rnb[i]:
                    #print(nums[i])
                    count+=1
        return count            
                