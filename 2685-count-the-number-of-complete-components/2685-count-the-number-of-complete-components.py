class Solution:
    #dfs with number of nodes and edges in a component and then check if it is connected componet nodes*nodes-1==edges
    def dfs(self,src,adj,visited,counte,countn):
        countn[0]+=1
        visited[src]=True
        for i in adj[src]:
            counte[0]+=1
            if visited[i]==False:
                self.dfs(i,adj,visited,counte,countn)
                
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[False for i in range(n)] 
        count=0
        adj=[[] for i in range(n)]
        for i in edges:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        for i in range(n):
            if visited[i]==False:
                counte=[0]
                countn=[0]
                self.dfs(i,adj,visited,counte,countn)
                print(countn,counte)
                if (countn[0])*(countn[0]-1)==counte[0]:
                    count+=1
        #print(visited)               
        return count   
        
        