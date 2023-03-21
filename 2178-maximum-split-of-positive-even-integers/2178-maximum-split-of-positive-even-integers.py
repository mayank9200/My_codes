class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2!=0:
            return []
        ans=[]
        currsumm=0
        i=0
        while currsumm+(2*(i+1))<=finalSum: #go till that point where the we found k-1 integers
            i+=1
            currsumm=currsumm+(2*i)
            ans.append(2*i) #making the ans
        #print(finalSum,currsumm) 
        ans[-1]=ans[-1]+(finalSum-currsumm)  #the last element will just be incremented by the remaining value  
        return ans
            
    