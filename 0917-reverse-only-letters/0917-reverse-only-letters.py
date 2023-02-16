class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        char=[]
        for k in s:
            char.append(k)
        while i<j:
            while i<len(s) and char[i].isalpha()==False:
                i+=1
            while j>=0 and char[j].isalpha()==False:
                j-=1
            if i>j:
                break
            char[i],char[j]=char[j],char[i]
            i+=1
            j-=1
        return ''.join(char)
                
        