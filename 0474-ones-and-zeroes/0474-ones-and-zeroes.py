class Solution:
    def countsubset(self,strs,ind,size,m,n,count,dp):
        if m<0 or n<0: #if going less than return 0
            return 0
        if ind==size: #if reaches end then we got a ans
            return 1
        if dp[ind][m][n]!=-1: #memorization
            return dp[ind][m][n]
        ones=0
        zeros=0
        for i in strs[ind]: #count of zeros and ones
            if i=='0':
                zeros+=1
            else:
                ones+=1
        dp[ind][m][n]=max(1+self.countsubset(strs,ind+1,size,m-zeros,n-ones,count,dp),self.countsubset(strs,ind+1,size,m,n,count,dp)) #max of taking and not taking is the ans
        return dp[ind][m][n]
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #https://www.youtube.com/watch?v=qkUZ87NCYSw
        size=len(strs)
        dp=[[[-1 for i in range(n+1)]for j in range(m+1)]for k in range(size+1)] #for memorization
        return self.countsubset(strs,0,size,m,n,count,dp)-1 #-1 because we consider an empty subset too
             
                    
                    
            
        