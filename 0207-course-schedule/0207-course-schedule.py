class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque
        q=deque()
        count=0
        indegree=[0 for i in range(numCourses)]
        adj=[[] for i in range(numCourses)]
        for i in prerequisites:
            indegree[i[0]]+=1
            adj[i[1]].append(i[0])
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                count+=1
        
        while len(q)>0:
            node=q.popleft()
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
                    count+=1
        return count==numCourses            
                    
        print(indegree)
        print(adj)
        return True
        