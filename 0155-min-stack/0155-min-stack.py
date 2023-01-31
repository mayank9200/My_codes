class MinStack:

    def __init__(self):
        self.arr=[]
        self.topp=-1
        self.minn=[]
        self.minntopp=-1
        

    def push(self, val: int) -> None:
        self.topp+=1
        self.arr.append(val)            
        if len(self.minn)==0 or val<=self.minn[self.minntopp]:
            self.minntopp+=1
            self.minn.append(val)   
        #print(self.arr)    
        
        
        
        

    def pop(self) -> None:
        if self.top==-1:
            return 0
        ele=self.arr[self.topp]
        if len(self.minn)>0 and self.minn[self.minntopp]==ele:
            self.minntopp-=1
            self.minn.pop()
        self.topp=self.topp-1
        self.arr.pop()
        #print(self.arr,self.minn)    
        
        

    def top(self) -> int:
        #print(self.arr,self.minn)    
        if len(self.arr)==0:
            return 0
        return self.arr[self.topp]
        

    def getMin(self) -> int:
        #print(self.arr,self.minn)    
        if len(self.minn)==0:
            return 0
        
        return self.minn[self.minntopp]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.topp()
# param_4 = obj.getMin()