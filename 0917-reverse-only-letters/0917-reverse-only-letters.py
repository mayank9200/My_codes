class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i=0
        j=len(s)-1
        char=[]
        for k in s:
            char.append(k) #making a character array
        while i<j:
            while i<len(s) and char[i].isalpha()==False: # move till not a alphabet
                i+=1
            while j>=0 and char[j].isalpha()==False: #move till not a aplhabet
                j-=1
            if i>j: #in between we cross each other
                break
            char[i],char[j]=char[j],char[i] #swapping
            i+=1
            j-=1
        return ''.join(char)
                
        