class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.premat=[[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(1,len(matrix[0])):
                self.premat[i][j]=self.premat[i][j]+self.premat[i][j-1]
        for j in range(len(matrix[0])):
            for i in range(1,len(matrix)):
                self.premat[i][j]=self.premat[i][j]+self.premat[i-1][j]        
        print(self.premat)        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summ=0
        if row1-1>=0 and col1-1>=0: 
            summ=self.premat[row2][col2]-self.premat[row1-1][col2]-self.premat[row2][col1-1]+self.premat[row1-1][col1-1]
        elif row1-1>=0:
            summ=self.premat[row2][col2]-self.premat[row1-1][col2]
        elif col1-1>=0:
            summ=self.premat[row2][col2]-self.premat[row2][col1-1]    
        #print(self.premat)
        else:
            summ=self.premat[row2][col2]
        
        return summ                         
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)