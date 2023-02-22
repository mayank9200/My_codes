class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #do it again
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i
