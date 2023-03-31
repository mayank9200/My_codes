class Solution:
    def reverseVowels(self, s: str) -> str:
        ans=''
        for i in s: 
            ii=i.lower()
            if ii in ['a','e','i','o','u']:
                ans+=i
        #print(ans)        
        ans=ans[::-1]
        fans=''
        k=0
        for i in s:
            ii=i.lower()
            if ii in ['a','e','i','o','u']:
                fans+=ans[k]
                k+=1
            else:
                fans+=i
        return fans        
            
        
        