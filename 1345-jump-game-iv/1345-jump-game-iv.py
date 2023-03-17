class Solution:
    def isvalid(self,i,n):
        return i>=0 and i<n
    def minJumps(self, arr: List[int]) -> int:
        from collections import deque
        q=deque()
        d={}
        n=len(arr)
        for i, num in enumerate(arr):
            if num not in d:
                d[num]=[i]
            else:    
                d[num].append(i)
        q.append(0)
        jump=0
        visited=set() #for particular index
        visited.add(0)
        visigrup=set() #for particular value(to optimize)
        while len(q)>0:
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node==n-1:
                    return jump
                first=node+1
                second=node-1
                if self.isvalid(first,n) and first not in visited: #go front
                    q.append(first)
                    visited.add(first)
                if self.isvalid(second,n) and second not in visited: #go back
                    q.append(second)
                    visited.add(second)   
                if arr[node] not in visigrup: #if that group of value is not visited
                    for k in d[arr[node]]: # go to all nodes with same values
                        if k!=node and k not in visited:
                            q.append(k)
                            visited.add(k) 
                    visigrup.add(arr[node])    #group of value is now visited
            jump+=1      
        return -1