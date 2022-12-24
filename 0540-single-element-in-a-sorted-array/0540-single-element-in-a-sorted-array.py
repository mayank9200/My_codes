class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-1]!=nums[n-2]:
            return nums[n-1]
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==nums[mid-1]:
                if mid%2!=0:
                    start=mid+1
                else:
                    end=mid-1
            elif nums[mid]==nums[mid+1]:
                if mid%2==0:
                    start=mid+1
                else:
                    end=mid-1
            else:
                return nums[mid]

                
                    
                    
                        
            
        