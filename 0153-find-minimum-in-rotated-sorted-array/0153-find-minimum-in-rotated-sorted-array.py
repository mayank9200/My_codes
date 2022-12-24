class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[0]<=nums[n-1]:
            return nums[0]
        start=0
        end=n-1
        while start<=end:
            #mid=end+(start-end)//2
            mid=(start+end)//2
            print(nums[mid])
            if mid-1>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            if mid+1<n and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            elif nums[start]<nums[mid]:
                start=mid+1
            else:
                end=mid-1
        return nums[mid]        
                