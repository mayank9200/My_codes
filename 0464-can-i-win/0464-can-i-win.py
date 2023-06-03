class Solution:
    
        #do again
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        if sum([i + 1 for i in range(maxChoosableInteger)]) < desiredTotal:
            return False

        @cache
        def dfs(total: int, mask: int) -> bool:
            canWin = False;
            for i in range(maxChoosableInteger):
                if mask >> i & 1 == 0:
                    if total + i + 1 >= desiredTotal:
                        canWin = True
                        break
                    newMask = mask | 1 << i
                    if not dfs(total + i + 1, newMask):
                        canWin = True
                        break
            return canWin
        
        return dfs(0, 0)