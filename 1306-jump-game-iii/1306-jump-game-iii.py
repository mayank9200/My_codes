class Solution:
    def isvalid(self,i,n):
        return i>=0 and i<n
    
    def canReach(self, arr: List[int], start: int) -> bool:
        from collections import deque
        n=len(arr)
        q=deque()
        q.append(start)
        visited=set()
        visited.add(start)
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if arr[node]==0:
                    return True
                if self.isvalid(node+arr[node],n) and node+arr[node] not in visited:
                    q.append(node+arr[node])
                    visited.add(node+arr[node])
                if self.isvalid(node-arr[node],n) and node-arr[node] not in visited:
                    q.append(node-arr[node])
                    visited.add(node-arr[node])
                    
        return False            
                
                
                
        