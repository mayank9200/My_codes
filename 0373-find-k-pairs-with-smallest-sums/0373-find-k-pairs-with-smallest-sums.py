class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        from heapq import heappush,heappop
        h=[]
        m=len(nums1)
        n=len(nums2)
        for i in range(m):
            heappush(h,[nums1[i]+nums2[0],i,0])
        ans=[]
        while len(ans)<k and len(h)>0:
            val,i,j=heappop(h)
            ans.append([nums1[i],nums2[j]])
            if j+1<n:
                heappush(h,[nums1[i]+nums2[j+1],i,j+1])
        return ans        