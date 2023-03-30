class Solution:
    def dfs(self,i,j,grid,visited):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or visited[i][j]==True or grid[i][j]=='0':
            return #coming out or grid or invalid position or already visited position
        visited[i][j]=True #make it visited
        #go to all 4 surrounging
        row=[1,-1,0,0]
        col=[0,0,1,-1]
        for k in range(4):    
            self.dfs(i+row[k],j+col[k],grid,visited)
        return 
        
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=[[False for i in range(n)]for j in range(m)]
        count=0
        for i in range(m):
            for j in range(n):
                if visited[i][j]==False and grid[i][j]=='1': #if valid
                    self.dfs(i,j,grid,visited)
                    count+=1
        return count        
        