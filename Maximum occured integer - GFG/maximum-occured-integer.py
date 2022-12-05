#User function Template for python3

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,L,R,N,maxx):
        arr=[0]*(maxx+10)
        for i in range(N):
            arr[L[i]]+=1
            arr[R[i]+1]-=1
        for i in range(1,len(arr)):
            arr[i]=arr[i]+arr[i-1]
        #print(arr)    
        index=0
        maxi=float('-inf')
        for i in range(len(arr)):
            if arr[i]>maxi:
                maxi=arr[i]
                index=i
        return index        
                
        
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math

A=[0]*1000000


            

def main():
    
    T=int(input())
    
    while(T>0):
        
        global A
        A=[0]*1000000
        
        N=int(input())
        
        L=[int(x) for x in input().strip().split()]
        R=[int(x) for x in input().strip().split()]
        
        maxx=max(R)
        ob=Solution()
        print(ob.maxOccured(L,R,N,maxx))
            
        
       
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends