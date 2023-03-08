class Solution:
    def isvalid(self,a):
        return a>=0 and a<=6000
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        from collections import deque
        q=deque()
        forbidden=set(forbidden)
        visited=set()
        q.append([0,False])
        visited.add((0,False))
        ans=0
        while len(q)>0:
            size=len(q)
            for i in range(size):
                curr,isback=q.popleft()
                if curr==x:
                    return ans
                if isback==False:
                    #move forward
                    if ((curr+a),False) not in visited and curr+a not in forbidden and self.isvalid(curr+a):
                        visited.add(((curr+a),False))
                        q.append([curr+a,False])
                    #move backward
                    if ((curr-b,True)) not in visited and curr-b not in forbidden and self.isvalid(curr-b):
                        visited.add(((curr-b),True))
                        q.append([curr-b,True])
                else:
                    #just move forward
                    if ((curr+a),False) not in visited and curr+a not in forbidden and self.isvalid(curr+a):
                        visited.add(((curr+a),False))
                        q.append([curr+a,False])
                        
            #print(visited)
            ans+=1            
        return -1                
                        
        