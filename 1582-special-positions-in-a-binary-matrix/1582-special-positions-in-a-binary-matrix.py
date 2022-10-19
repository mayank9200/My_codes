class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m=len(mat)
        n=len(mat[0])
        no_one_row=[0 for i in range(m)]
        no_one_col=[0 for i in range(n)]
        for i in range(m):
            for j in range(n):
                no_one_row[i]+=mat[i][j]
        for j in range(n):
            for i in range(m):
                no_one_col[j]+=mat[i][j]  
        count=0
        for i in range(m):
            for j in range(n):
                if mat[i][j]==1 and no_one_row[i]==1 and no_one_col[j]==1:
                    count+=1
        return count            
        