#User function Template for python3

class Solution:
    def dfs(self,i,adj,visited):
        visited[i]=True
        for j in adj[i]:
            if visited[j]==False:
                self.dfs(j,adj,visited)
      
    def numProvinces(self, adj, V):
        n=len(adj)
        visited=[False for i in range(n)]
        adjj=[[] for i in range(n)]
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if adj[i][j]==1 and i!=j:
                    adjj[i].append(j)
                    adjj[j].append(i)
        for i in range(n):
            if visited[i]==False:
                self.dfs(i,adjj,visited)
                count+=1        
        return count
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        V=int(input())
        adj=[]
        
        for i in range(V):
            temp = list(map(int,input().split()))
            adj.append(temp);
        
        ob = Solution()
        print(ob.numProvinces(adj,V))
# } Driver Code Ends