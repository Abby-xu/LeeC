class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        arrows, end = 0, -float('inf')
        for i in points:
            if i[0] > end:
                arrows += 1
                end = i[1]
        return arrows
