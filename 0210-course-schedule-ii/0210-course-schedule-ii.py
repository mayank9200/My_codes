class Solution:
    #simple topological sort printing
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque
        q=deque()
        count=0
        indegree=[0 for i in range(numCourses)] #storing indegrees
        adj=[[] for i in range(numCourses)] #adj list
        ans=[]
        count=0
        for i in prerequisites:
            indegree[i[0]]+=1
            adj[i[1]].append(i[0])
        for i in range(numCourses):
            if indegree[i]==0: #if indegree is 0 put in queue
                q.append(i)
                ans.append(i)
                count+=1
        
        while len(q)>0:
            node=q.popleft() 
            for i in adj[node]:
                indegree[i]-=1 #reduce indegree
                if indegree[i]==0: #if indegree becomes 0 append it to queue
                    q.append(i)
                    count+=1
                    ans.append(i)
        if count!=numCourses:
            return []
        return ans   #print topological sort order    