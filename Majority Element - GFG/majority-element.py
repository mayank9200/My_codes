#User function template for Python 3

class Solution:
    def majorityElement(self, A, N):
        count=0
        maj=0
        for i in A:
            if i==maj:
                count+=1
            elif count==0:
                maj=i
                count+=1
            else:
                count-=1
        c=0
        for i in A:
            if i==maj:
                c+=1
        if c>(N//2):
            return maj
        else:
            return -1
                  
        #Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
        T=int(input())
        while(T>0):
            
            N=int(input())

            A=[int(x) for x in input().strip().split()]
            
            
            obj = Solution()
            print(obj.majorityElement(A,N))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends