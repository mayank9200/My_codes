#User function Template for python3

class Solution:
    def dfs(self,visited,src,adj,ans):
        ans.append(src)
        visited[src]=True
        for i in adj[src]:
            if visited[i]==False:
                self.dfs(visited,i,adj,ans)
                
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited=[False]*V
        ans=[]
        for i in range(V):
            if visited[i]==False:
                self.dfs(visited,i,adj,ans)
        return ans        
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends