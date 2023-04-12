class Solution:
    def digitCount(self, num: str) -> bool:
        n=len(num)
        d={}
        for i in num:
            d[int(i)]=d.get(int(i),0)+1
        
        ans=''
        for i in range(n):
            if i not in d:
                d[i]=0
        for i in range(n):
            ans=ans+str(d[i])
 
        return num==ans
            
              
       
        