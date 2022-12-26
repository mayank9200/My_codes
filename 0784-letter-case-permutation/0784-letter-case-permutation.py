class Solution:
    def rec(self,s,pos,res,ans):
        if pos==len(s):
            res.append(ans)
            return 
        if s[pos].isalpha():
            self.rec(s,pos+1,res,ans+s[pos].lower())
            self.rec(s,pos+1,res,ans+s[pos].upper())
        else:
            self.rec(s,pos+1,res,ans+s[pos])
            
    def letterCasePermutation(self, s: str) -> List[str]:
        pos=0
        ans=''
        res=[]
        self.rec(s,pos,res,ans)
        return res
        