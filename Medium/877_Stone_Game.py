class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        ifAlex = True
        alex = lee = 0
        left = 0
        right = len(piles) - 1
        
        while left < right:
            if piles[left] > piles[right]:
                if ifAlex: alex += piles[left]
                else: lee += piles[left]
                left += 1
            else:
                if ifAlex: alex += piles[right]
                else: lee += piles[right]
                right -= 1
            
            ifAlex = ~ifAlex
        
        return alex > lee

'''
The simplest: return True
Since Alex always chooses the stone first, he can always choose the large one
'''