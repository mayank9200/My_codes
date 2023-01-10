class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start=0
        n=len(nums)
        end=len(nums)-1
        while start<end:
            #print(nums,start,end)
            while start<n and nums[start]%2==0:
                start+=1
                print(start)
            while end>=0 and nums[end]%2!=0:
                print(end)
                end-=1
            print(start,end)    
            if start>=end:
                return nums
            nums[start],nums[end]=nums[end],nums[start]
        return nums     
        