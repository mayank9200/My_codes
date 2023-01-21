class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n==1:
            return 1
        dp=[0]*(n+1)
        dp[1]=1
        p2=1
        p3=1
        p5=1
        i=2
        while i<=n:
            t1=dp[p2]*2
            t2=dp[p3]*3
            t3=dp[p5]*5
            minn=min(t1,t2,t3)
            dp[i]=minn
            if t1==minn:
                p2+=1
            if t2==minn:
                p3+=1
            if t3==minn:
                p5+=1
            i+=1    
        return dp[n]         
                
        
        