class Solution:
    #floydd warshal algorithm
    #mat=shortest distance from i to j considering all paths
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat=[[float('inf') for i in range(n)]for j in range(n)]
        for edge in edges:
            mat[edge[0]][edge[1]]=edge[2]
            mat[edge[1]][edge[0]]=edge[2]
        for i in range(n):
            mat[i][i]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j]=min(mat[i][j],mat[i][k]+mat[k][j]) #direct or via k, which is smaller
        res=0
        totcount=float('inf')
        for i in range(n):
            tcount=0
            for j in range(n):
                if mat[i][j]!=0 and mat[i][j]<=distanceThreshold: #in each col, how many are less than threshold
                    tcount+=1
            if tcount<=totcount: 
                res=i
                totcount=tcount
        return res        
    
    #TC: O(n^3)