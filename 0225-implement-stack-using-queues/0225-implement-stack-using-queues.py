class MyStack:
    from collections import deque

    def __init__(self):
        self.s=deque()
        

    def push(self, x: int) -> None:
        i=0
        self.s.append(x)
        while i<len(self.s)-1:
            self.s.append(self.s.popleft())
            i+=1
            
        

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