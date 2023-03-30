class Solution:
    def isvalid(self,i,j,m,n,visited,mat):
        return i>=0 and j>=0 and i<m and j<n and visited[i][j]==False and mat[i][j]==1
    def bfs(self,mat):
        from collections import deque
        q=deque()
        m=len(mat)
        n=len(mat[0])
        visited=[[False for i in range(n)]for j in range(m)]
        ans=[[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j,0])
                    visited[i][j]=True
        while len(q)>0:
            size=len(q)
            for _ in range(size):
                i,j,count=q.popleft()
                if self.isvalid(i+1,j,m,n,visited,mat):
                    q.append([i+1,j,count+1])
                    visited[i+1][j]=True
                    ans[i+1][j]=count+1
                if self.isvalid(i-1,j,m,n,visited,mat):
                    q.append([i-1,j,count+1])
                    visited[i-1][j]=True
                    ans[i-1][j]=count+1
                if self.isvalid(i,j+1,m,n,visited,mat):
                    q.append([i,j+1,count+1])
                    visited[i][j+1]=True
                    ans[i][j+1]=count+1
                if self.isvalid(i,j-1,m,n,visited,mat):
                    q.append([i,j-1,count+1])
                    visited[i][j-1]=True    
                    ans[i][j-1]=count+1
        return ans           
        
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        return self.bfs(mat)
        