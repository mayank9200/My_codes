class Solution:
    def dfs(self,i,j,grid,m,n,tans):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0 or grid[i][j]==-1: #if going out of range or water is surrounded or visited
            return 
        tans[0]+=1 #count that cell
        grid[i][j]=-1 #make it visited
        self.dfs(i+1,j,grid,m,n,tans)
        self.dfs(i,j+1,grid,m,n,tans)
        self.dfs(i-1,j,grid,m,n,tans)
        self.dfs(i,j-1,grid,m,n,tans)
        return 
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxx=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                tans=[0]
                if grid[i][j]==1:
                    self.dfs(i,j,grid,m,n,tans)
                    maxx=max(maxx,tans[0])
        return maxx            
        
        