class Solution:
    def mergesort(self,arr,left,mid,right,count):
        i=left
        j=mid+1
        ans=[]
        while i<=mid and j<=right:
            if arr[i]<=arr[j]:
                ans.append(arr[i])
                i+=1
            else:
                ans.append(arr[j])
                count[0]+=(mid-i+1)
                j+=1
        while i<=mid:
            ans.append(arr[i])
            i+=1
        while j<=right:
            ans.append(arr[j])
            j+=1
        i=left
        for k in range(len(ans)):
            arr[i]=ans[k]
            i+=1
        return    
            
            
    def merge(self,arr,left,right,count):
        if right>left:
            mid=(left+right)//2
            self.merge(arr,left,mid,count)
            self.merge(arr,mid+1,right,count)
            self.mergesort(arr,left,mid,right,count)
        
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
      #                 [2,4,1,3,4]
        #      [2,4,1]                [3,4].       [1,2,4] [3,4]
        # [2,4]         [1]      [3]       [4]         
    def inversionCount(self, arr, n):
        count=[0]
        self.merge(arr,0,n-1,count)
        return (count[0])    
        return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends