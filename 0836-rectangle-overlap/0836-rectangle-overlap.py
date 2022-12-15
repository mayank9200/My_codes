class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=map(int,rec1)
        x3,y3,x4,y4=map(int,rec2)
        hori=False
        vert=False
        if max(x1,x3)<min(x2,x4):
            hori=True
        if max(y1,y3)<min(y2,y4):
            vert=True
        return hori and vert    
        
       