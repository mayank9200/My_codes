# just start dfs from all 4 sides element and mark the islands from that point, all that will be 0 only, rest all will be one
class Solution:
    def dfs(self,i,j,board):
        m=len(board)
        n=len(board[0])
        if i<0 or j<0 or i>=m or j>=n or board[i][j]=='X' or board[i][j]=='.':
            return 
        board[i][j]='.'
        #print(board)
        row=[1,-1,0,0]
        col=[0,0,1,-1]
        for k in range(4):
            nrow=i+row[k]
            ncol=j+col[k]
            self.dfs(nrow,ncol,board)
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if i==0 or j==0 or i==m-1 or j==n-1:
                    self.dfs(i,j,board)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='.':
                    board[i][j]='O'
        print(board)
        return 
        """
        Do not return anything, modify board in-place instead.
        """
        