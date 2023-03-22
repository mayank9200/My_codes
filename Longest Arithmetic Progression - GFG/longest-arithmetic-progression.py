#User function Template for python3

class Solution:
    def lengthOfLongestAP(self, A, n):
        #https://www.youtube.com/watch?v=Y3sZ2bsresI
        n=len(A)
        dp=[{} for i in range(n)] #each place is a dictionary containing the difference and their frequency before them ([{}, {3: 1}, {6: 1, 3: 2}, {9: 1, 6: 1, 3: 3}])
        maxx=0
        for i in range(n):
            for j in range(i):
                val=A[i]-A[j]
                if val in dp[j]: #if the diff is previously also seen
                    dp[i][val]=dp[j][val]+1 #increment by one by taking current diff
                else:
                    dp[i][val]=1 #just add this as new diff for this element
                maxx=max(maxx,dp[i][val]) #max value till now 
        #print(dp) #print karke dekho sb smaj jaoge
        return maxx+1 #maxx is freq so values are freq+1
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        A = list(map(int, input().split()))
        ob = Solution()
        ans = ob.lengthOfLongestAP(A, n)
        print(ans)
        tc -= 1

# } Driver Code Ends