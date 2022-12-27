class Solution:
    
    def grayCode(self, n: int) -> List[int]:
        # res=[]
        # if n==0:
        #     retrun [0]
        # res.append(0)
        # res.append(1)
        # for i in range(1,n):
        #     temp=pow(2,i)
        #     l=len(res)
        #     for j in range(l-1,-1,-1):
        #         res.append(res[j]+temp)
        # return res   
        if n==0:
            return [0]
        if n==1:
            return [0,1]
        asf=self.grayCode(n-1)
        l=len(asf)
        for i in range(l-1,-1,-1):
            temp=pow(2,n-1)
            asf.append(asf[i]+temp)
        return asf    
            
        