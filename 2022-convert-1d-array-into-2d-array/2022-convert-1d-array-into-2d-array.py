class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original)!=m*n:
            return []
        mat=[[0 for j in range(n)] for i in range(m)]
        k=0
        for i in range(m):
            for j in range(n):
                mat[i][j]=original[k]
                k+=1
        return mat        
        