class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        d={}
        for i,j in enumerate(secret):
            if j not in d:
                d[j]=set()
                d[j].add(i)
            else:
                d[j].add(i)
        b=0
        c=0
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                b+=1
                if secret[i] in d:
                    d[secret[i]].remove(i)
                    if len(d[secret[i]])==0:
                        d.pop(secret[i])
        for i in range(len(guess)):
            if guess[i] in d and secret[i]!=guess[i]:
                c+=1
                for j in d[guess[i]]:
                    d[guess[i]].remove(j)
                    break
                if len(d[guess[i]])==0:
                    d.pop(guess[i])
        return ''.join([str(b),'A',str(c),'B'])   