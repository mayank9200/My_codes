class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxx=float('-inf')
        for i in range(len(accounts)):
            maxx=max(maxx,sum(accounts[i]))
        return maxx    
                
        