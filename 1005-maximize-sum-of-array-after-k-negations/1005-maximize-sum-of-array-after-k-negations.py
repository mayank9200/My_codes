class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort() #sort
        for i in range(n):
            if k==0: #break at 0
                break
            if nums[i]<0:
                nums[i]=-1*nums[i] #starting se positive banate jao
                k=k-1
        minn=float('inf')  
        summ=0
        for i in range(n):
            summ+=nums[i]
            minn=min(minn,nums[i]) #find what is current minimum
        if k%2!=0:
            return summ-2*minn #subtract two times as it was added earlier
        else:
            return summ            
        
                