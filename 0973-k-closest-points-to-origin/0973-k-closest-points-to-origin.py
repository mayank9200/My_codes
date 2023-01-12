class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        from heapq import heappush, heappop
        h=[]
        c=0
        for i in points:
            heappush(h,[-(i[0]**2+i[1]**2),i[0],i[1],c])
            if len(h)>k:
                heappop(h)
        ans=[]
        while len(h)>0:
            temp=heappop(h)
            ans.append([temp[1],temp[2]])
        return ans    