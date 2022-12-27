class Solution:
    def grayCode(self, n: int) -> List[int]:
        res=[]
        if n==0:
            retrun [0]
        res.append(0)
        res.append(1)
        for i in range(1,n):
            temp=pow(2,i)
            ans=[]
            for j in range(len(res)-1,-1,-1):
                ans.append(res[j]+temp)
            res=res+ans
        return res    
            
            
        