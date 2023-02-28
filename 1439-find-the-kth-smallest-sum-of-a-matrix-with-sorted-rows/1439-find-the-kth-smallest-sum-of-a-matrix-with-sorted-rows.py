class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        from collections import deque
        q=deque()
        h=[]
        m=len(mat)
        n=len(mat[0])
        for i in mat[0]:
            q.append(i)
        row=0    
        while len(q)>0:
            size=len(q)
            row+=1
            if row==m:
                break
            for i in range(size):
                val=q.popleft()
                for col in range(n):
                    q.append(val+mat[row][col])
            ans=[]
            while len(q)>0:
                ans.append(q.popleft())
            ans.sort()
            if len(ans)>k:
                ans=ans[:k]
            for i in ans:
                q.append(i)
        return q[-1]