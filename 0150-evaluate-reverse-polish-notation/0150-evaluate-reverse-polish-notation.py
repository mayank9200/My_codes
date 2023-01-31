class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from collections import deque
        s=deque()
        for i in tokens:
            if i!='+' and i!='-' and i!='*' and i!='/':
                s.appendleft(int(i))
            else:
                op1=s.popleft()
                op2=s.popleft()
                if i=='+':
                    val=op2+op1
                elif i=='-':
                    val=op2-op1
                elif i=='*':
                    val=op2*op1
                elif i=='/':    
                    val=int(op2/op1)
                    
                s.appendleft(val)
        return s[0]        
                    
                    
        