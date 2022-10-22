class Solution:
    def ismatch(self,st,i):
        if st[0]=='(' and i==')':
            return True
        elif st[0]=='[' and i==']':
            return True
        elif st[0]=='{' and i=='}':
            return True
        return False
    def isValid(self, s: str) -> bool:
        from collections import deque
        st=deque()
        for i in s:
            if i=='(' or i=='[' or i=='{':
                st.appendleft(i)
            elif i==')'or i=='}' or i==']':
                if len(st)==0:
                    return False
                elif len(st)>0 and self.ismatch(st,i):
                    st.popleft()
                elif len(st)>0 and self.ismatch(st,i)==False:
                    return False
        print(st)
        if len(st)==0:
            return True
        return False
        