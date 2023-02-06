class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        arr=[]
        for i in range(len(profit)):
            arr.append([difficulty[i],profit[i]])
        arr.sort()
        worker.sort() #important
        summ=0
        i=0
        maxx=0
        tot=0
        n=len(profit)
        for work in worker:
            while i<n and arr[i][0]<=work: #greedy
                maxx=max(maxx,arr[i][1])
                i+=1
            tot=tot+maxx   #final ans loading   
        return tot
        