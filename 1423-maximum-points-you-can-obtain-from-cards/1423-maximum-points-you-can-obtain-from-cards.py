class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        #total me se n-k window subtract krke jo max ans ho, try to visualize its easy
        total=sum(cardPoints)
        wind_sum=0
        n=len(cardPoints)
        for i in range(n-k):
            wind_sum+=cardPoints[i]
        i=0
        j=(n-k-1)
        ans=0
        while j<n:
            ans=max(ans,total-wind_sum) #check first case
            if j+1<n:
                wind_sum+=cardPoints[j+1] #add j
            if i+1<n:
                wind_sum-=cardPoints[i] #remove i
            j+=1
            i+=1
        return ans    
            
        