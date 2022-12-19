class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        l1=0
        l2=0
        l3=0
        l4=0
        if max(ax1,bx1)<min(ax2,bx2):
            l1,l3=max(ax1,bx1),min(ax2,bx2)
        if max(ay1,by1)<min(ay2,by2):
            l2,l4=max(ay1,by1),min(ay2,by2)
        
        # print(l1,l2,l3,l4)    
        # print((ax2-ax1)*(ay2-ay1))
        # print(((bx2-bx1)*(by2-by1)))
        # print(((l3-l1)*(l4-l2)))
        return ((ax2-ax1)*(ay2-ay1))+((bx2-bx1)*(by2-by1))-((l3-l1)*(l4-l2))
        