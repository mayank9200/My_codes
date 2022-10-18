class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        temp2=-1
        while low<=high:
            mid=(low+high)//2
            if  nums[mid]==target:
                temp2=mid
                high=mid-1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        low=0
        high=len(nums)-1
        temp1=-1
        while low<=high:
            mid=(low+high)//2
            if  nums[mid]==target:
                temp1=mid
                low=mid+1
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1    
        return [temp2,temp1]        
        
        