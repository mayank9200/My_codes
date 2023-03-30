class Solution:
    def isvalid(self,i,j,m,n,grid,visited):
        return i>=0 and j>=0 and i<m and j<n and grid[i][j]==0 and visited[i][j]==False 
    def bfs(self,grid):
        if grid[0][0]==1:
            return -1
        from collections import deque
        q=deque()
        m=len(grid)
        n=len(grid[0])
        visited=[[False for i in range(n)]for j in range(m)]
        q.append([0,0,1])
        visited[0][0]=True
        while len(q)>0:
            i,j,step=q.popleft()
            if i==m-1 and j==n-1:
                return step
            row=[1,-1,0,0,1,-1,1,-1]
            col=[0,0,1,-1,-1,1,1,-1]
            for k in range(8):
                nrow=i+row[k]
                ncol=j+col[k]
                if self.isvalid(nrow,ncol,m,n,grid,visited):
                    visited[nrow][ncol]=True
                    q.append([nrow,ncol,step+1])
                    
        return -1
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        return self.bfs(grid)
        