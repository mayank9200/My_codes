class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[]
        if n==0:
            retrun [0]
        res.append(0)
        res.append(1)
        for i in range(1,n):
            temp=pow(2,i)
            l=len(res)
            for j in range(l-1,-1,-1):
                res.append(res[j]+temp)
        return res    
            
            
        