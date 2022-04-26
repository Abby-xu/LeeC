class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size, res, papa = max(map(max, points)), [], {}
        find = lambda x: x if x == papa.setdefault(x, x) else (papa.__setitem__(x, find(papa[x])) or papa[x])
        union = lambda a, b: papa.__setitem__(find(a), find(b))
        edges = sorted((abs(xa - xb) + abs(ya - yb), (xa, ya), (xb, yb)) for (xa, ya), (xb, yb) in itertools.combinations(points, 2))
        return sum(union(a, b) or cost for cost, a, b in edges if find(a) != find(b))
