class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        ans=''
        for j,i in enumerate(num):
            if int(i)>=change[int(i)]:
                ans=ans+str(int(i))
            else:
                break    
        while j<len(num) and change[int(num[j])]>=int(num[j]):
            ans=ans+str(change[int(num[j])])
            j+=1
        while j<len(num):
            ans=ans+num[j]
            j+=1
        #print(i,j)            
        # while j<len(num):
        #     ans=ans+num[j] 
        #     j+=1    
        return ans[:len(num)]  
                
        