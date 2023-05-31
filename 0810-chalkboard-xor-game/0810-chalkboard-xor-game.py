class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        #do again
        xor = 0
        for i in nums: xor ^= i
        return xor == 0 or len(nums) % 2 == 0
        