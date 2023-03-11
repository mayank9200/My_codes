class Solution:
    def reverse(self,start,end,nums):
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    def rotate(self, nums: List[int], k: int) -> None:
        start=0
        end=len(nums)-1
        d=(len(nums)-k)%len(nums)
        self.reverse(start,d-1,nums)
        self.reverse(d,end,nums)
        self.reverse(start,end,nums)
        return nums

        """
        Do not return anything, modify nums in-place instead.
        """