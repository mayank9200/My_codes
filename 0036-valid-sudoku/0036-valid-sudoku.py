class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                val=board[i][j]
                for k in range(9):
                    if k!=i:
                        if board[k][j]==val:
                            return False
                for k in range(9):
                    if k!=j: 
                        if board[i][k]==val:
                            return False
                si=(i//3)*3
                ei=(j//3)*3
                for p in range(si,si+3):
                    for q in range(ei,ei+3):
                        if p==i and q==j:
                            continue
                        if board[p][q]==val:
                            return False      
        return True            
                
                        
                
                
        