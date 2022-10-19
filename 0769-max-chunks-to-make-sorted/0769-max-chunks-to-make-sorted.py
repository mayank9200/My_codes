class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        maxtillnow=-1
        count=0
        for i in range(n):
            maxtillnow=max(maxtillnow,arr[i])
            if i==maxtillnow:
                count+=1
        return count       