class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=n-1
        if len(nums)==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        while start<=end:
            mid=end+(start-end)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid+1]>nums[mid-1]:
                start=mid+1
            else:
                end=mid-1
        return -1        
        