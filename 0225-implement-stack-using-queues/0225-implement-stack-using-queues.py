class MyStack:
    from collections import deque

    def __init__(self):
        self.s=deque()
        

    def push(self, x: int) -> None:
        sq=deque()
        while len(self.s)>0:
            val=self.s.popleft()
            sq.append(val)
        self.s.append(x)
        while len(sq)>0:
            val=sq.popleft()
            self.s.append(val)
            
        

    def pop(self) -> int:
        val=self.s.popleft()
        return val

    def top(self) -> int:
        if len(self.s)==0:
            return -1
        return self.s[0]
        

    def empty(self) -> bool:
        if len(self.s)==0:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()