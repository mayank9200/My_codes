class Solution:
    def isvalid(self,i,j,m,n):
        return i>=0 and j>=0 and i<m and j<n #to check if it goes out of the island
    def dfs(self,i,j,grid,peri):
        m=len(grid)
        n=len(grid[0])
        if self.isvalid(i,j,m,n)==False or grid[i][j]==0: #if goes out or surrounding is water then increase peri
            peri[0]+=1
            return
        if grid[i][j]==-1: #if reached a visited cell
            return
        grid[i][j]=-1 #make visited
        #go to all 4 directions

        self.dfs(i+1,j,grid,peri)
        self.dfs(i,j+1,grid,peri)
        self.dfs(i-1,j,grid,peri)
        self.dfs(i,j-1,grid,peri)
        return
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri=[0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    self.dfs(i,j,grid,peri)
       
        return peri[0]
        #do again
        