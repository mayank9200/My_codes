class MyQueue:
    from collections import deque

    def __init__(self):
        self.s=deque()

    def push(self, x: int) -> None:
        st=deque()
        while len(self.s)>0:
            val=self.s.popleft()
            st.appendleft(val)
        self.s.appendleft(x)
        while len(st)>0:
            val=st.popleft()
            self.s.appendleft(val)
        

    def pop(self) -> int:
        if self.empty():
            return -1
        val=self.s.popleft()
        return val
           
        
        

    def peek(self) -> int:
        if self.empty():
            return -1
        return self.s[0]
        

    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()