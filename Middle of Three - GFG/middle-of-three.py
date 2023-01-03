#User function Template for python3

class Solution:
    def middle(self,A,B,C):
        x=A-B
        y=B-C
        z=C-A
        if x*y>0:
            return B
        elif y*z>0:
            return C
        else:
            return A


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        A,B,C=map(int,input().strip().split())
        ob=Solution()
        print(ob.middle(A,B,C))
# } Driver Code Ends