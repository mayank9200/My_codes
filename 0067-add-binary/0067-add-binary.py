class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=a[::-1]
        b=b[::-1] 
        carry=0
        i=0
        j=0
        fans=''
        m,n=len(a),len(b)
        if m<n:
            a=a+'0'*(n-m)
        elif m>n:
            b=b+'0'*(m-n)     
        # print(a)
        # print(b)
        for i in range(len(a)):
            if int(a[i])+int(b[i])+carry==3:
                carry=1
                fans+='1'
            elif int(a[i])+int(b[i])+carry==2:
                carry=1
                fans+='0' 
            elif int(a[i])+int(b[i])+carry==1:
                carry=0
                fans+='1'
            else:
                carry=0
                fans+='0'
        if carry==1:
            fans+='1'    
        return fans[::-1]        
                
            