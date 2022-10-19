class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        arr=[[] for i in range(len(matrix[0]))]
        for i in range(n):
            for j in range(len(matrix[0])):
                arr[j].append(matrix[i][j])
        return arr        
                
        