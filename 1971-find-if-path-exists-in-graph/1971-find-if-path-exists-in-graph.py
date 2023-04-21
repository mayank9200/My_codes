class Solution:
    #simple dfs will work here
    def dfs(self,src,dest,adj,visited):
        visited[src]=True
        if src==dest:
            return True
        for i in adj[src]:
            if visited[i]==False and self.dfs(i,dest,adj,visited)==True:
                return True
        return False    
            
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        visited=[False for i in range(n)]
        return self.dfs(source,destination,adj,visited)
        
        
        