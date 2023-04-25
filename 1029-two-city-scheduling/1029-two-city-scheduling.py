class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda a:(a[1]-a[0]),reverse =True)
        ans=0
        #print(costs)
        for i in range((len(costs)//2)):
            ans+=costs[i][0]
        for i in range(len(costs)//2,len(costs)):
            ans+=costs[i][1]
        return ans    
        