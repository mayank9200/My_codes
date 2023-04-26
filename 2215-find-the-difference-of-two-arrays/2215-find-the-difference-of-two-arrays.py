class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans=[set(),set()]
        d1=set()
        d2=set()
        for i in nums1:
            d1.add(i)
        for i in nums2:
            d2.add(i)
        for i in nums1:
            if i not in d2:
                ans[0].add(i)
        for i in nums2:
            if i not in d1:
                ans[1].add(i)
        ans[0]=list(ans[0])
        ans[1]=list(ans[1])
        return ans
                
            
        