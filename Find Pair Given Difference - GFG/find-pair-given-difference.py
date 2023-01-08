#User function Template for python3

class Solution:

    def findPair(self, arr, L,N):
        arr.sort() #[2,3,5,20,80] 
        i=0
        j=1
        while j<L and i<L:
            if arr[j]-arr[i]==N:
                return True
            elif arr[j]-arr[i]<N:
                j+=1
            else:
                i+=1
                if i==j:
                    j+=1
        return False        
            
        #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        L,N = [int(x) for x in input().split()]
        arr = [int(x) for x in input().split()]

        solObj = Solution()

        if(solObj.findPair(arr,L, N)):
            print(1)
        else:
            print(-1)
# } Driver Code Ends