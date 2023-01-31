class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #exact same as stock span problem
        from collections import deque
        s=deque()
        ngl=[]
        ans=[]
        res=[]
        n=len(temperatures)
        for i in range(n-1,-1,-1):
            if len(s)>0 and temperatures[s[0]]>temperatures[i]:
                ans.append(s[0])
            else:
                while len(s)>0 and temperatures[s[0]]<=temperatures[i]:
                    s.popleft()
                if len(s)==0:
                    ans.append(-1)
                else:
                    ans.append(s[0])
            s.appendleft(i)
        ans=ans[::-1]
        for i in range(n):
            if ans[i]==-1:
                res.append(0)
            else:    
                res.append(ans[i]-i)
        return res    
        