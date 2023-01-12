class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxx=float('-inf')
        count=0
        for i in range(len(arr)):
            maxx=max(maxx,arr[i])
            if i==maxx:
                count+=1
            
        return count        