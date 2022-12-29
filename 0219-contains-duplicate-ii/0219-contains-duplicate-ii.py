class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        j=0
        n=len(nums)
        s=set()
        while j<n:
            if nums[j] in s:
                return True
            if (j-i+1)<k+1:
                s.add(nums[j])
                j+=1
            else:
                s.add(nums[j])
                s.remove(nums[i])
                i+=1
                j+=1   
                
        return False        
                
                
                