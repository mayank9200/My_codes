class Solution:
    import math
    def solve(self,num):
        fact=[]
        summ=0
        for i in range(1,int(math.sqrt(num))+1):
            if num%i==0:
                if i!=num//i:
                    fact.append(i)
                    fact.append(num//i)
                else:
                    fact.append(i)
                summ=summ+i+num//i
                if len(fact)>4:
                    break
        #print(fact)        
        if len(fact)==4:
            return summ
        return 0
            
        
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            temp=self.solve(i)
            #print(temp)
            if temp!=0:
                ans+=temp
        return ans        
        
        