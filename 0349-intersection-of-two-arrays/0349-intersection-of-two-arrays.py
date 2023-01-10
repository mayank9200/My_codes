class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        ans=[]
        for i in nums1:
            d[i]=d.get(i,0)+1
        for i in nums2:
            if i in d:
                d.pop(i)
                ans.append(i)
        return ans        
        