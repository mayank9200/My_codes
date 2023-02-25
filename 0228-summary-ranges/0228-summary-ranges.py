class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        #do it again
        if not nums:
            return []

        res = []
        start, i = nums[0], 1
        while i < len(nums):
            if nums[i] - nums[i - 1] != 1:
                res.append(str(start) + '->' + str(nums[i - 1]) if start != nums[i - 1] else str(start))
                start = nums[i]
            i += 1
        res.append(str(start) + '->' + str(nums[i - 1]) if start != nums[i - 1] else str(start))

        return res
