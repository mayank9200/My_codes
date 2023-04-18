class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(src,dest,d,visited,prod):
            if src==dest:
                return prod[0]
            visited.add(src)
            for i in d[src]:
                if i[0] not in visited:
                    prod[0]=prod[0]*i[1]
                    tans=dfs(i[0],dest,d,visited,prod)
                    prod[0]=prod[0]/i[1]
                    if tans!=-1:
                        return tans
            return -1
        d={}
      
        n=len(values)
        for i in range(n):
            if equations[i][0] not in d:
                d[equations[i][0]]=[[equations[i][1],values[i]]]
            else:
                d[equations[i][0]].append([equations[i][1],values[i]])
                
            if equations[i][1] not in d:
                d[equations[i][1]]=[[equations[i][0],1/values[i]]]
            else:
                d[equations[i][1]].append([equations[i][0],1/values[i]])
        ans=[]
        print(d)
        for q in queries:
            prod=[1]
            visited=set()
            if q[0] not in d or q[1] not in d:
                ans.append(-1.0)
            else:    
                val=dfs(q[0],q[1],d,visited,prod)
                ans.append(val)     
        return ans