#User function Template for python3


class Solution:
    def dfs(self,i,parent,visited,adj,rec):
        visited[i]=True
        rec[i]=True
        for j in adj[i]:
            if visited[j]==False:
                if self.dfs(j,i,visited,adj,rec)==True:
                        return True
            elif rec[j]==True:
                return True
        rec[i]=False            
        return False
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        visited=[False for i in range(V)]
        rec=[False for i in range(V)]
	    for i in range(V):
	        if visited[i]==False:
	            if self.dfs(i,-1,visited,adj,rec)==True:
	                return True
	    return False    
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
        
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        V,E = list(map(int, input().strip().split()))
        adj = [[] for i in range(V)]
        for i in range(E):
            a,b = map(int,input().strip().split())
            adj[a].append(b)
        ob = Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)
# } Driver Code Ends