class Solution:
    def isvalid(self,row,col,n,mat):
        i=row-1
        j=col
        while i>=0 and j>=0:
            if mat[i][j]=='Q':
                return False
            i-=1
        i=row-1
        j=col-1
        while i>=0 and j>=0 and row<n and col<n:
            if mat[i][j]=='Q':
                return False
            i-=1
            j-=1
        i=row-1
        j=col+1
        while i>=0 and j>=0 and i<n and j<n:
            if mat[i][j]=='Q':
                return False
            i-=1    
            j+=1
        return True    
            
        
        
    def rec(self,pos,n,mat,res,count):
        if pos==n:
            count[0]+=1
            return
        for i in range(n):
            if self.isvalid(pos,i,n,mat):
                mat[pos][i]='Q'
                self.rec(pos+1,n,mat,res,count)
                mat[pos][i]='.'
                
        
    def totalNQueens(self, n: int) -> int:
        mat=[['.' for i in range(n)] for j in range(n)]
        res=[]
        count=[0]
        self.rec(0,n,mat,res,count)
        return count[0]
        