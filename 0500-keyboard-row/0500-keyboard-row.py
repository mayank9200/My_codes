class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        #simple
        
        d={}
        ans=[]
        s=['qwertyuiop','asdfghjkl','zxcvbnm']
        for i in range(len(s)):
            for j in s[i]:
                d[j]=i
                d[j.upper()]=i     
        for i in words:
            found=False
            temp=d[i[0]]
            for j in i:
                if d[j]==temp:
                    continue
                found=True
                break
                
            if found==False:
                ans.append(i)
        return ans        
                    
        