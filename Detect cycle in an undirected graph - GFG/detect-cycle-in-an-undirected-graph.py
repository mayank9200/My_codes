from typing import List
class Solution:
    def dfs(self,i,parent,visited,adj):
        visited[i]=True
        for j in adj[i]:
            if j!=parent and visited[j]==True:
                return True
            else:
                if visited[j]==False:
                    if self.dfs(j,i,visited,adj)==True:
                        return True
        return False                
                
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    visited=[False for i in range(V)]
	    for i in range(V):
	        if visited[i]==False:
	            if self.dfs(i,-1,visited,adj)==True:
	                return True
	    return False         
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends