class Solution:
    #topological sort to check if there is no cycle in directed graph
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        q=deque()
        count=0
        indegree=[0 for i in range(numCourses)] #storing indegrees
        adj=[[] for i in range(numCourses)] #adj list
        for i in prerequisites:
            indegree[i[0]]+=1
            adj[i[1]].append(i[0])
        for i in range(numCourses):
            if indegree[i]==0: #if indegree is 0 put in queue
                q.append(i)
                count+=1
        
        while len(q)>0:
            node=q.popleft()
            for i in adj[node]:
                indegree[i]-=1 #reduce indegree
                if indegree[i]==0: #if indegree becomes 0 append it to queue
                    q.append(i)
                    count+=1
        return count==numCourses   #see if all nodes are visited         
                    
      
        