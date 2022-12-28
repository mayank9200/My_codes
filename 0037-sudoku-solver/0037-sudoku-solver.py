class Solution:
    import sys
    sys.setrecursionlimit(10**6)
    def isvalid(self,board,row,col,num,n):
        for i in range(n):
            if i!=row and board[i][col]==num:
                return False
        for j in range(n):
            if j!=col and board[row][j]==num:
                return False
        top=(row//3)*3
        left=(col//3)*3
        for i in range(top,top+3):
            for j in range(left,left+3):
                if board[i][j]==num:
                    return False
        return True        
    
        
        
        
    def solveSudoku(self, board: List[List[str]]) -> None:
        n=len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j]==".":
                    for k in range(1,10):
                        if self.isvalid(board,i,j,str(k),n):
                            #print(i,j,k)
                            board[i][j]=str(k)
                            if self.solveSudoku(board):
                                return True
                            board[i][j]="."
                    return False    
        return True
        """
        Do not return anything, modify board in-place instead.
        """
        