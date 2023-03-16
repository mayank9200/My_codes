class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dpbs=[0 for i in range(n)]
        dpss=[0 for i in range(n)]
        dpcs=[0 for i in range(n)]
        dpbs[0]=-prices[0]
        for i in range(1,n):
            dpbs[i]=max(dpbs[i-1],dpcs[i-1]-prices[i])
            dpss[i]=max(dpss[i-1],dpbs[i-1]+prices[i])
            dpcs[i]=max(dpcs[i-1],dpss[i-1])
        return max(dpss[n-1],dpcs[n-1])    
        