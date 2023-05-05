#User function Template for python3

class Solution:
    def isPossible(self,N,prerequisites):
        from collections import deque
        q=deque()
        count=0
        indegree=[0 for i in range(N)] #storing indegrees
        adj=[[] for i in range(N)] #adj list
        for i in prerequisites:
            indegree[i[0]]+=1
            adj[i[1]].append(i[0])
        for i in range(N):
            if indegree[i]==0: #if indegree is 0 put in queue
                q.append(i)
                count+=1
        
        while len(q)>0:
            node=q.popleft()
            for i in adj[node]:
                indegree[i]-=1 #reduce indegree
                if indegree[i]==0: #if indegree becomes 0 append it to queue
                    q.append(i)
                    count+=1
        return count==N   #see if all nodes are visited 
        #code here
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N=int(input())
        P=int(input())

        prerequisites=[]
        for _ in range(P):
            pair = [int(x) for x in input().split()]
            prerequisites.append(pair)
        ob=Solution()
        if(ob.isPossible(N,prerequisites)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends