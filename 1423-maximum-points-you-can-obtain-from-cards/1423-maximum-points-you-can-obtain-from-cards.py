class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        wind_sum=0
        n=len(cardPoints)
        for i in range(n-k):
            wind_sum+=cardPoints[i]
        i=0
        j=(n-k-1)
        ans=0
        while j<n:
            ans=max(ans,total-wind_sum)
            if j+1<n:
                wind_sum+=cardPoints[j+1]
            if i+1<n:
                wind_sum-=cardPoints[i]
            j+=1
            i+=1
        return ans    
            
        