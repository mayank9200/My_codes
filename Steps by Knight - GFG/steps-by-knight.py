class Solution:
    def isvalid(self,i,j,n,visited):
        return i>=0 and j>=0 and i<n and j<n and visited[i][j]==False

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    from collections import deque
	    q=deque()
	    visited=[[False for i in range(N)]for j in range(N)]
	    q.append([KnightPos[0]-1,KnightPos[1]-1,0])
	    visited[KnightPos[0]-1][KnightPos[1]-1]=True
	    step=1
	    row=[2,-2,2,-2,1,-1,1,-1]
	    col=[1,-1,-1,1,2,-2,-2,2]
	    while len(q)>0:
	        node=q.popleft()
	        
	        if node[0]==TargetPos[0]-1 and node[1]==TargetPos[1]-1:
	            return node[2]
	        for i in range(8):
	            nrow=node[0]+row[i]
	            ncol=node[1]+col[i]
	            if self.isvalid(nrow,ncol,N,visited):
	                visited[nrow][ncol]=True
	                q.append([nrow,ncol,node[2]+1])
	    return -1         
		#Code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		KnightPos = list(map(int, input().split()))
		TargetPos = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minStepToReachTarget(KnightPos, TargetPos, N)
		print(ans)

# } Driver Code Ends