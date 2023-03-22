class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        #https://www.youtube.com/watch?v=Y3sZ2bsresI
        n=len(nums)
        dp=[{} for i in range(n)] #each place is a dictionary containing the difference and their frequency before them ([{}, {3: 1}, {6: 1, 3: 2}, {9: 1, 6: 1, 3: 3}])
        maxx=0
        for i in range(n):
            for j in range(i):
                val=nums[i]-nums[j]
                if val in dp[j]: #if the diff is previously also seen
                    dp[i][val]=dp[j][val]+1 #increment by one by taking current diff
                else:
                    dp[i][val]=1 #just add this as new diff for this element
                maxx=max(maxx,dp[i][val]) #max value till now 
        #print(dp) #print karke dekho sb smaj jaoge
        return maxx+1 #maxx is freq so values are freq+1
        