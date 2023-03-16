class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #https://www.youtube.com/watch?v=pTQB9wbIpfU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=32
        n=len(prices)
        dpbs=[0 for i in range(n)]
        dpss=[0 for i in range(n)]
        dpbs[0]=-prices[0]
        dpss[0]=0
        for i in range(1,n):
            dpbs[i]=max(dpbs[i-1],dpss[i-1]-prices[i])
            dpss[i]=max(dpss[i-1],dpbs[i-1]+prices[i]-fee)
        return dpss[n-1]    

            