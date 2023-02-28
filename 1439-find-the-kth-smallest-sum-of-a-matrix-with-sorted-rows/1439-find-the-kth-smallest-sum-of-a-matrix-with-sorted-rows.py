class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        from collections import deque
        q=deque()
        h=[]
        m=len(mat)
        n=len(mat[0])
        for i in mat[0]: #simply put qst row in queue
            q.append(i)
        row=0    
        while len(q)>0: #bfs apply
            size=len(q)
            row+=1
            if row==m: #if we beyond last row
                break
            for i in range(size):
                val=q.popleft()
                for col in range(n): #making combinations of elements in queue and next row values
                    q.append(val+mat[row][col])
            ans=[]
            while len(q)>0: #putting queue in array so that we can sort it
                ans.append(q.popleft())
            ans.sort() #sort
            if len(ans)>k:
                ans=ans[:k] #keep values till k only in queue
            for i in ans: #put back in queue
                q.append(i)
        return q[-1] #last element of queue is our ans