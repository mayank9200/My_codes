class Solution:
    #https://www.youtube.com/watch?v=UagRoA3C5VQ&list=PL-Jc9J83PIiEZvXCn-c5UIBvfT8dA-8EG
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        dp=[[0 for i in range(n)] for j in range(m)]
        maxx=0
        for i in range(m):
            dp[i][0]=1 if matrix[i][0]=='1' else 0       
            maxx=max(maxx,dp[i][0])
        for i in range(n):
            dp[0][i]=1 if matrix[0][i]=='1' else 0  
            maxx=max(maxx,dp[0][i])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='1':
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) #min wale ke sath milke ek bada square bana lega
                maxx=max(maxx,dp[i][j])    
          
        return maxx*maxx