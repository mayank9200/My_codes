class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda a: a[1],reverse=True)
        summ=0
        count=0
        for i in boxTypes:
            if count+i[0]<truckSize:
                count=count+i[0]
                summ=summ+i[1]*i[0]
                print(summ)
            else:
                val=truckSize-count
                summ=summ+i[1]*val
                #print(summ)
                count=count+i[0]
                break
        return summ       