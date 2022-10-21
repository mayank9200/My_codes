class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heappush,heappop
        h=[]
        n=len(matrix)
        for i in range(n):
            heappush(h,[matrix[i][0],i,0])
        ans=0    
        while len(h)>0 and ans<k:
            val,i,j=heappop(h)
            j=j+1
            ans+=1
            if ans==k:
                return val
            if j<n:
                heappush(h,[matrix[i][j],i,j])
        return val        
                    
            
        
        