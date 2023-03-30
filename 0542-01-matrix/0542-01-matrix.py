class Solution:
    def isvalid(self,i,j,m,n,visited,mat):
        return i>=0 and j>=0 and i<m and j<n and visited[i][j]==False and mat[i][j]==1
    def bfs(self,mat):
        from collections import deque
        q=deque()
        m=len(mat)
        n=len(mat[0])
        visited=[[False for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    visited[i][j]=True
        while len(q)>0:
            size=len(q)
            for _ in range(size):
                i,j,count=q.popleft()
                row=[1,-1,0,0]
                col=[0,0,1,-1]
                for k in range(4):
                    nrow=i+row[k]
                    ncol=j+col[k]
                    if self.isvalid(nrow,ncol,m,n,visited,mat):
                        q.append([nrow,ncol,count+1])
                        visited[nrow][ncol]=True
                        mat[nrow][ncol]=count+1
        return mat           
        
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.bfs(mat)
        