class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        gs,ss = sorted(g),sorted(s)
        c = 0
        while ss and gs:
            if ss[-1] >= gs[-1]:
                ss.pop()
                c += 1
            gs.pop()
        return c