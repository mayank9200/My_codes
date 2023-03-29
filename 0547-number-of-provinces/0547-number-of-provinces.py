class Solution:
    def dfs(self,i,adj,visited):
        visited[i]=True
        for j in adj[i]:
            if visited[j]==False:
                self.dfs(j,adj,visited)
      
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited=[False for i in range(n)]
        adj=[[] for i in range(n)]
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        for i in range(n):
            if visited[i]==False:
                self.dfs(i,adj,visited)
                count+=1        
        return count
                
        