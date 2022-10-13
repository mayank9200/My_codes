class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dirr=0
        arr=[[0 for i in range(n)] for j in range(n)]
        top=0
        left=0
        right=n-1
        bottom=n-1
        k=1
        while top<=bottom and left<=right:
            if dirr==0:
                for i in range(left,right+1):
                    arr[top][i]=k
                    k+=1
                top+=1
            elif dirr==1:
                for i in range(top,bottom+1):
                    arr[i][right]=k
                    k+=1
                right-=1
            elif dirr==2:
                for i in range(right,left-1,-1):
                    arr[bottom][i]=k
                    k+=1
                bottom-=1
            elif dirr==3:
                for i in range(bottom,top-1,-1):
                    arr[i][left]=k
                    k+=1
                left+=1  
            dirr=(dirr+1)%4
        return arr    
                