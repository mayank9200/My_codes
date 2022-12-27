class Solution:
    #2-['a','b','c']
    def rec(self,pos,ip,op,res,d):
        if pos==len(ip):
            res.append(op)
            return 
        for i in d[ip[pos]]:
            self.rec(pos+1,ip,op+i,res,d)
            
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        d={}
        val=ord('a')
        for i in range(2,7):
            count=0
            i=str(i)
            d[i]=''
            while count<3:
                d[i]=d[i]+chr(val)
                val+=1
                count+=1     
        val=ord('p')
        for i in range(7,10):
            count=0
            i=str(i)
            d[i]=''
            if i=='8':
                while count<3:
                    d[i]=d[i]+chr(val)
                    val+=1
                    count+=1 
            else:
                while count<4:
                    d[i]=d[i]+chr(val)
                    val+=1
                    count+=1
        op=''
        res=[]
        self.rec(0,digits,op,res,d)      
        return res