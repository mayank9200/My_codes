class Solution:
    def check(self,position,mid,m):
        curr=position[0]
        count=1
        for i in range(1,len(position)):
            if position[i]-curr>=mid:
                curr=position[i]
                count+=1
        #print(count)        
        if count<m:
            return False
        return True
                
    def maxDistance(self, position: List[int], m: int) -> int:
        start=1
        end=max(position)
        candidate=start
        position.sort() 
        while start<=end:
            mid=(start+end)//2
            if self.check(position,mid,m):
                #print(mid)
                candidate=mid
                start=mid+1
            else:
                end=mid-1
        return candidate         
        