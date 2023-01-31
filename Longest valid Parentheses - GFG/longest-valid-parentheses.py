# User function Template for Python3

class Solution:
    def maxLength(self, S):
        from collections import deque
        st=deque()
        st.appendleft(-1)
        maxx=0
        for i in range(len(S)):
            if S[i]=='(':
                st.appendleft(i)
            else:
                st.popleft()
                if len(st)==0:
                    st.appendleft(i) #insert new invalid index
                else:
                    maxx=max(maxx,i-st[0])
                   
        return maxx  
        # code here


#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()
        
        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends