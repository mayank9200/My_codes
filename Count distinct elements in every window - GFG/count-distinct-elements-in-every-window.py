
class Solution:
    def countDistinct(self, A, N, K):
        ans=0
        i=0
        j=0
        d={}
        ans=[]
        while j<n:
            d[A[j]]=d.get(A[j],0)+1
            if (j-i+1)<k:
                j+=1
            elif j-i+1==k:    
                ans.append(len(d))
                d[A[i]]-=1
                if d[A[i]]==0:
                    d.pop(A[i])
                i+=1
                j+=1
        return ans        
            
        # Code here


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends