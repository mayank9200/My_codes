class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        from collections import deque
        s=deque()
        tans=[]
        n=len(prices)
        for i in range(n-1,-1,-1):
            if len(s)==0:
                s.appendleft(prices[i])
                tans.append(0)
            else:
                while len(s)>0 and s[0]>prices[i]:
                    s.popleft()
                if len(s)==0:
                    tans.append(0)
                else:
                    tans.append(s[0])
                s.appendleft(prices[i])    
        tans=tans[::-1]
        for i in range(n):
            tans[i]=prices[i]-tans[i]
        return tans    