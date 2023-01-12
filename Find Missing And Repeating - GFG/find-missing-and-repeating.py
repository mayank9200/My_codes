#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        xor=0
        for i in arr:
            xor=xor^i
        for i in range(1,n+1):
            xor=xor^i
        res1=0
        res2=0
        mask=xor&(-xor)
        for i in arr:
            if i&mask:
                res1=res1^i
            else:
                res2=res2^i
        for i in range(1,n+1):
            if i&mask:
                res1=res1^i
            else:
                res2=res2^i
        for i in arr:
            if i==res1:
                repeating=i
                missing=res2
            if i==res2:
                repeating=i
                missing=res1
        return [repeating,missing]
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends