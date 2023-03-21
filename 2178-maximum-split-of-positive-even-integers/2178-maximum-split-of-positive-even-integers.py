class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        s=deque()
        if finalSum%2!=0:
            return []
        ans=[]
        currsumm=0
        i=0
        while currsumm+(2*(i+1))<=finalSum:
            i+=1
            currsumm=currsumm+(2*i)
            ans.append(2*i)
        #print(finalSum,currsumm) 
        ans[-1]=ans[-1]+(finalSum-currsumm)    
        return ans
            
    