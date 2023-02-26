class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush,heappop
        h=[]
        for i in stones:
            heappush(h,-i)
        while len(h)>=2:
            t1=-heappop(h)
            t2=-heappop(h)
            if t1!=t2:
                heappush(h,-abs(t2-t1))
        if len(h)>0:
            return -h[0]
        return 0