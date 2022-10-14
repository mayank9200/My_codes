class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row=set()
        cols=set()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    cols.add(j)
        for i in row:
            for j in range(n):
                matrix[i][j]=0
        for i in cols:
            for j in range(m):
                matrix[j][i]=0
        return matrix        
            
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        