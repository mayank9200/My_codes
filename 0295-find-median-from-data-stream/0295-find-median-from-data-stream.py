class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        

    def addNum(self, num: int) -> None:
        from heapq import heappush,heappop
        if len(self.maxheap)==len(self.minheap):
            heappush(self.maxheap,-num)
        else:
            heappush(self.minheap,num)
        if len(self.maxheap)==0 or len(self.minheap)==0:
            return
        if -self.maxheap[0]>self.minheap[0]: #just check top of both heap, maxheap top should be less than min heap top
            t1=-heappop(self.maxheap)
            t2=heappop(self.minheap)
            heappush(self.maxheap,-t2)
            heappush(self.minheap,t1)
            
            
        

    def findMedian(self) -> float: #simply find median
        if len(self.maxheap)==len(self.minheap):
            return (-1*self.maxheap[0]+self.minheap[0])/2
        else:
            return -1*self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()