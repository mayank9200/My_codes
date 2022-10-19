class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        i=0
        j=n-1
        found=False
        while i>=0 and j>=0 and i<m and j<n:
            if target==matrix[i][j]:
                found=True
                break
            elif target<matrix[i][j]:
                j=j-1
            else:
                i=i+1
        return found        
        