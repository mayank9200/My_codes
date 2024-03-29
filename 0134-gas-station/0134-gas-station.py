class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        currpet=0
        prevpet=0
        i=0
        start=0
        n=len(gas)
        for i in range(n):
            currpet=currpet+(gas[i]-cost[i])
            if currpet<0:
                start=i+1
                prevpet=prevpet+currpet
                currpet=0
        if currpet+prevpet>=0:
            return start
        return -1
        