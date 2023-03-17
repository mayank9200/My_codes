class Solution:
    def isvalid(self,i,n):
        return i>=0 and i<n
    def minJumps(self, arr: List[int]) -> int:
        from collections import deque
        q=deque()
        d={}
        n=len(arr)
        d = defaultdict(list)
        for i, num in enumerate(arr):
            d[num].append(i)
        q.append(0)
        jump=0
        visited=set()
        visited.add(0)
        visigrup=set()
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node==n-1:
                    return jump
                first=node+1
                second=node-1
                if self.isvalid(first,n) and first not in visited:
                    q.append(first)
                    visited.add(first)
                if self.isvalid(second,n) and second not in visited:
                    q.append(second)
                    visited.add(second)   
                if arr[node] not in visigrup:
                    for k in d[arr[node]]:
                        if k not in visited:
                            q.append(k)
                            visited.add(k)
                    visigrup.add(arr[node])    
            jump+=1      
        return -1
#         def minJumps(self, arr):
#             n = len(arr)
#             d = defaultdict(list)
#             for i, num in enumerate(arr):
#                 d[num].append(i)

#             queue = deque([(0, 0)])
#             visited, visited_groups = set(), set()

#             while queue:
#                 steps, index = queue.popleft()
#                 if index == n - 1: return steps

#                 for neib in [index - 1, index + 1]:
#                     if 0 <= neib < n and neib not in visited:
#                         visited.add(neib)
#                         queue.append((steps + 1, neib))

#                 if arr[index] not in visited_groups:
#                     for neib in d[arr[index]]:
#                         if neib not in visited:
#                             visited.add(neib)
#                             queue.append((steps + 1, neib))
#                     visited_groups.add(arr[index])