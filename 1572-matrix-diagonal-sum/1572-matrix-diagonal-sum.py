class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        summ=0
        for i in range(n):
            summ+=mat[i][i]+mat[i][n-1-i]
        if n%2!=0:
            return summ-mat[n//2][n//2]
        else:
            return summ
        
        