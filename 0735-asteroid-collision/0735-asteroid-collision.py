class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        #do it again
        stack = []
        for num in asteroids:
            if num>0:
                stack.append(num)
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(num):
                    stack.pop()
                if not stack or stack[-1]<0:
                    stack.append(num)
                elif stack[-1] == -num:
                    stack.pop()
        return stack
        # from collections import deque
        # s=deque()
        # ans=[]
        # for i in asteroids:
        #     if i>0:
        #         s.appendleft(i)
        #     else:
        #         while len(s)>0 and abs(i)>s[0] and s[0]<abs(i):
        #             s.popleft()
        #         if len(s)==0 or s[0]<0:
        #             s.appendleft(i)
        #         elif s[0]==-i:
        #             s.popleft()
        # ans=[]
        # while len(s)>0:
        #     ans.append(s.popleft())
        # return ans[::-1]    
                    
                    
            