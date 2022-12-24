class Solution:
    #Take 2 stacks, one is freq stack and other is char stack,as soon as we see ],pop top of char stack and frequency stack and appendleft result in char stack, (dont forget to push whole number in freq stack rather than single digit, check line 13)
    def decodeString(self, s: str) -> str:
        from collections import deque
        s1=deque()
        s2=deque()
        n=len(s)
        i=0
        while i<n:
            if s[i].isdigit():
                j=i
                val=''
                while s[j].isdigit(): #calculating number
                    val=val+s[j]
                    j+=1
                i=j-1
                s1.appendleft(int(val))   
            elif s[i]==']':
                temp1=''
                while s2[0]!='[':
                    temp1=s2[0]+temp1
                    s2.popleft()
                s2.popleft()
                temp2=s1.popleft()
                s2.appendleft(temp2*temp1)
            else:
                s2.appendleft(s[i])
            i+=1    
            #print(s1,s2)
        res=''
        while len(s2)!=0:
            res=s2[0]+res
            s2.popleft()
        return res
        