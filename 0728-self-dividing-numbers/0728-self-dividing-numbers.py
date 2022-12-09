class Solution:
    def solve(self,num):
        val=num
        i=1
        while num>0:
            temp=num%10
            num=num//10
            if temp==0:
                return False
            if val%temp!=0:
                return False
        return True    
            
            
            
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            if self.solve(i)==True:
                ans.append(i)
        return ans        
                
        