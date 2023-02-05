class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr=[]
        for i in range(len(profit)):
            arr.append([difficulty[i],profit[i]])
        arr.sort()
        worker.sort()      
        maxx=0
        for i in arr:
            maxx=max(maxx,i[1])
        summ=0
        i=0
        maxx=0
        tot=0
        n=len(profit)
        for work in worker:
            while i<n and arr[i][0]<=work:
                maxx=max(maxx,arr[i][1])
                i+=1
            tot=tot+maxx      
        return tot
        