class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s=''
        temp=ord('A')
        while columnNumber>0:
            columnNumber=columnNumber-1
            val=columnNumber%26
            s=s+chr(val+temp)
            #s=s+chr(val-ord('A'))
            
            columnNumber=columnNumber//26
        return s[::-1]    
            
        