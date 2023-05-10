#User function Template for python3

class Solution:
    def parentrec(self,i,parent):
        if parent[i]==i:
            return i
        return self.parentrec(parent[i],parent)    
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        parent=[]
        edge=[]
        s=set()
        for i in range(V):
            parent.append(i)
        for i in range(len(adj)):
            for j in adj[i]:
                if (i,j[0]) not in s or (j[0],i) not in s:
                    edge.append([i,j[0],j[1]])
                    s.add((i,j[0]))
                    s.add((j[0],i))
        ss=0
        i=0
        summ=0
        
        edge.sort(key=lambda a:a[2])
        #print(edge)
        while ss<V-1:
            x=edge[i][0]
            y=edge[i][1]
            px=self.parentrec(x,parent)
            py=self.parentrec(y,parent)
            if px!=py:
                summ=summ+edge[i][2]
                parent[py]=px
                ss+=1
            i+=1
        return summ    
            
        
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        ob = Solution()
        
        print(ob.spanningTree(V,adj))
# } Driver Code Ends