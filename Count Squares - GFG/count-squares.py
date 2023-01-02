#User function Template for python3

class Solution:
    def countSquares(self, N):
        start=1
        end=N
        candi=0
        while start<=end:
            mid=(start+end)//2
            #print(start,end,mid)
            if mid*mid==N:
                break
            elif mid*mid<N:
                candi=mid
                start=mid+1
            else:
                end=mid-1
        return candi
        # code here 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.countSquares(N))
# } Driver Code Ends