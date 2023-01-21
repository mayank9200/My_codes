class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        from heapq import heappush,heappop
        h=[]
        ans=[]
        n=len(arr)
        for i in range(n):
            heappush(h,[abs(arr[i]-x),i])
        while len(h)>0 and k>0:
            k=k-1
            temp=heappop(h)
            ans.append(arr[temp[1]])
        ans.sort()
        return ans
                     