class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n=len(arr)
        leftmax=[float('-inf')]*n
        rightmin=[float('inf')]*n
        leftmax[0]=arr[0]
        rightmin[n-1]=arr[n-1]
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],arr[i])
        for i in range(n-2,-1,-1):
            rightmin[i]=min(rightmin[i+1],arr[i])
        #print(leftmax,rightmin)
        i=0
        j=1
        count=0
        while j<n:
            if leftmax[i]<=rightmin[j]:
                count+=1
            i+=1
            j+=1
        return count+1    
        
        