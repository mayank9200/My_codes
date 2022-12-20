class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        start=0
        end=m-1
        candidate=0
        while start<=end:  
            mid=(start+end)//2
            #print(matrix[mid][n-1])
            if target==matrix[mid][n-1]:
                return True
            elif matrix[mid][n-1]<target:
                start=mid+1
            else:
                candidate=mid
                end=mid-1
        start=0
        end=n-1
        while start<=end:
            mid=(start+end)//2
            if matrix[candidate][mid]==target:
                return True
            elif target<matrix[candidate][mid]:
                end=mid-1
            else:
                start=mid+1
        return False        
                
        