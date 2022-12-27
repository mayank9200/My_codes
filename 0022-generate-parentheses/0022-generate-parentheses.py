class Solution:
    def rec(self,op,res,openb,closedb):
        if openb<0 or closedb<0:
            return
        if openb==0 and closedb==0:
            res.append(op)    
            return 
        self.rec(op+'(',res,openb-1,closedb)
        if openb<closedb:
            self.rec(op+')',res,openb,closedb-1)
            
    def generateParenthesis(self, n: int) -> List[str]:
        op=''
        res=[]
        openb=n
        closedb=n
        self.rec(op,res,openb,closedb)
        return res
        