#User function Template for python3

class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        arr=[]
        for i in range(n):
            arr.append([start[i],end[i]])
        arr.sort(key=lambda a:a[1])
        count=1
        j=0
        for i in range(1,n):
            if arr[i][0]>arr[j][1]:
                count+=1
                j=i
        return count        
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends