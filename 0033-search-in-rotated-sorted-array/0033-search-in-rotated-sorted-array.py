class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        start=0
        end=n-1
        while start<=end:
            mid=end+(start-end)//2
            if target==nums[mid]:
                return mid
            elif nums[start]<=nums[mid]:
                if target>=nums[start] and target<=nums[mid]:
                    end=mid-1
                else:
                    start=mid+1
            else:
                if target>=nums[mid] and target<=nums[end]:
                    start=mid+1
                else:
                    end=mid-1
        return -1            
        