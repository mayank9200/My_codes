class Solution:
    def longestValidParentheses(self, s: str) -> int:
        from collections import deque
        st=deque()
        st.appendleft(-1)
        maxx=0
        for i in range(len(s)):
            if s[i]=='(':
                st.appendleft(i)
            else:
                st.popleft()
                if len(st)==0:
                    st.appendleft(i) #insert new invalid index
                else:
                    maxx=max(maxx,i-st[0])
                   
        return maxx        
        