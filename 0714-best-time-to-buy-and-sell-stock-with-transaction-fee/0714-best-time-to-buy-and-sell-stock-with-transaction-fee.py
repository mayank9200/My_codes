class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #https://www.youtube.com/watch?v=pTQB9wbIpfU&list=PL-Jc9J83PIiG8fE6rj9F5a6uyQ5WPdqKy&index=32
        #maintain two states
        # one brought state where brought> sell
        # one sell state where brought=sell
        #see gradually how current result depends on previous result
#         [-1, -1, -1, -1, 1, 1]
#         [0, 0, 0, 5, 5, 8]
        
        
        n=len(prices)
        dpbs=[0 for i in range(n)]
        dpss=[0 for i in range(n)]
        dpbs[0]=-prices[0] #buy state
        dpss[0]=0 #sell state
        for i in range(1,n):
            dpbs[i]=max(dpbs[i-1],dpss[i-1]-prices[i]) #either take previous bought state or buy current stock over previous selling
            dpss[i]=max(dpss[i-1],dpbs[i-1]+prices[i]-fee) #either take previous selling or sell the previous bought by deducting the fee
        return dpss[n-1]    

            