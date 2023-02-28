class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set()
        for i in candyType:
            s.add(i)
        req=len(candyType)//2
        return min(req,len(s))
        