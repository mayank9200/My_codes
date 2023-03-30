class Solution:
    def isvalid(self,i,j,m,n,grid,visited):
        return i>=0 and j>=0 and i<m and j<n and grid[i][j]==1 and visited[i][j]==False
    from collections import deque
    def bfs(self,grid,visited):
        m=len(grid)
        n=len(grid[0])
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j,0])
                    visited[i][j]=True
        print(q)
        maxx=0
        while len(q)>0:
            size=len(q)
            for _ in range(size):
                i,j,sec=q.popleft()
                maxx=max(maxx,sec)
                if self.isvalid(i+1,j,m,n,grid,visited):
                    q.append([i+1,j,sec+1])
                    visited[i+1][j]=True
                if self.isvalid(i-1,j,m,n,grid,visited):
                    q.append([i-1,j,sec+1])
                    visited[i-1][j]=True
                if self.isvalid(i,j+1,m,n,grid,visited):
                    q.append([i,j+1,sec+1])
                    visited[i][j+1]=True
                if self.isvalid(i,j-1,m,n,grid,visited):
                    q.append([i,j-1,sec+1])
                    visited[i][j-1]=True    
        return maxx           
                
        
        
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        ans=self.bfs(grid,visited)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if visited[i][j]==False and grid[i][j]!=0 :
                    return -1
        return ans
        
        