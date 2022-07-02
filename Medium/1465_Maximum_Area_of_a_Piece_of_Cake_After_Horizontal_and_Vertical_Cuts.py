class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return ((m:=lambda v: max(a-b for a,b in zip(v[1:],v)))([0]+sorted(horizontalCuts)+[h])*m([0]+sorted(verticalCuts)+[w]))%(10**9+7)