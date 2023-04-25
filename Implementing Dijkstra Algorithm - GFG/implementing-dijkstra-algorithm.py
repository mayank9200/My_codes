class Solution:
    def minn(self,V,adj,visited,dist):
        ind=0
        minn=float('inf')
        for i in range(V):
            if visited[i]==False and dist[i]<=minn:
                minn=dist[i]
                ind=i
        return ind        
        

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        from heapq import heappush,heappop
        h=[]
        visited=[False for i in range(V)]
        dist=[float('inf') for i in range(V)]
        dist[S]=0
        for i in range(V):
            u=self.minn(V,adj,visited,dist)
            visited[u]=True
            for v in adj[u]:
                if dist[u]+v[1]<dist[v[0]]:
                    dist[v[0]]=dist[u]+v[1]
        return dist
                    
                    
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends