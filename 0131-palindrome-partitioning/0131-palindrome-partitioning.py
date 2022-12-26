class Solution:
    def ispalin(self,s):
        start=0
        end=len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                return False
            start+=1
            end-=1
        return True
    def rec(self,ip,ans,res,):
        if len(ip)==0:
            res.append(ans[:])
            return 
        
        for i in range(len(ip)):   
            first_half=ip[0:i+1]
            second_half=ip[i+1:]
            if self.ispalin(first_half):  
                ans.append(first_half)
                self.rec(second_half,ans,res)
                ans.pop()

            
            
        
    def partition(self, s: str) -> List[List[str]]:
        op=''
        res=[]
        ans=[]
        self.rec(s,ans,res)
        return res