#User function Template for python3

class Solution:
    def isvalid(self,i,j,m,n,visited):
        return i>=0 and j>=0 and i<n and j<n and visited[i][j]==False and m[i][j]==1
    def backtrack(self,i,j,m,n,visited,ans,tans):
        if self.isvalid(i,j,m,n,visited)==False:
            return 
        if i==n-1 and j==n-1:
            ans.append(tans)
        visited[i][j]=True    
        self.backtrack(i+1,j,m,n,visited,ans,tans+'D')  
        self.backtrack(i-1,j,m,n,visited,ans,tans+'U') 
        self.backtrack(i,j+1,m,n,visited,ans,tans+'R') 
        self.backtrack(i,j-1,m,n,visited,ans,tans+'L') 
        visited[i][j]=False
    def findPath(self, m, n):
        ans=[]
        tans=''
        visited=[[False for i in range(n)] for j in range(n)]
        self.backtrack(0,0,m,n,visited,ans,tans)
        return ans
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends