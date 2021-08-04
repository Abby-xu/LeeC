class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        parents = [i for i in range(n+1)]
        
        # add pipes to each house from the well, node zero.
        for i, cost in enumerate(wells):
            pipes.append([0, i+1, cost])
        
        # run kruskal algo to build minimum spanning tree.
        # first, sort by cost
        # start picking the lowest cost edges until we visited all nodes.
        pipes.sort(key=lambda x:x[2])
                
        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u
        
        def union(u, v):
            pu = find(u)
            pv = find(v)
            
            if pu != pv:
                parents[pu] = pv
            return
        
        res = 0
        
        for u, v, cost in pipes:
            if find(u) != find(v):
                union(u, v)
                res += cost
        return res