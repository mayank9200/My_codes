#User function Template for python3

class Solution:
    def countBits(self, N, A):
        summ=0
        for i in range(64):
            cones,czeros=0,0
            for j in A:
                if j&(1<<i):
                    #print('y')
                    cones+=1
                else:
                    czeros+=1
            summ=summ+(cones*czeros*2)
      
        return summ%(1000000007)    
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()
        for it in range(N):
            A[it] = int(A[it])
        
        ob = Solution()
        print(ob.countBits(N, A))
# } Driver Code Ends