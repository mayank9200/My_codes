class Solution:
    def checkRecord(self, s: str) -> bool:
        counta=0
        countl=0
        foundl=False
        n=len(s)
        for i in range(n):
            if s[i]=='A':
                counta+=1
            if s[i]=='L':
                countl+=1
                if countl==3:
                    foundl=True
            else:
                countl=0
        if counta>=2 or foundl==True:
            return False
        return True
        