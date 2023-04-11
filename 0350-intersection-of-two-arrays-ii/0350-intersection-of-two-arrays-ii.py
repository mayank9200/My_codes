class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        ans=[]
        for i in nums1:
            d[i]=d.get(i,0)+1
        for i in nums2:
            if i in d:
                ans.append(i)
                d[i]-=1
                if d[i]==0:
                    d.pop(i)
        return ans            