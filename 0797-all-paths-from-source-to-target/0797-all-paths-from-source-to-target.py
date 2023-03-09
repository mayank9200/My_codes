class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque
        n=len(graph)
        q=deque()
        q.append([0,[0]])
        ans=[]
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node,tlist=q.popleft()
                if node==n-1:
                    ans.append(tlist)
                for j in graph[node]:
                    q.append([j,tlist+[j]])
        return ans            
                    
                
                
        
        