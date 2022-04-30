class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d,ans = {},[]
        for ind,(x,y) in enumerate(equations):
            val = values[ind]
            if x not in d: d[x] = {y:val}
            else: d[x][y] = val
            if y not in d: d[y] = {x:1/val}
            else: d[y][x] = 1/val
 
        for x,y in queries:
            if x not in d or y not in d:
                ans.append(-1.0)
            elif x in d and y in d:
                stack,seen,found = [(x,1.0)],{x},0
                while stack:
                    x,ratio = stack.pop()
                    if y in d[x]:
                        ans.append(d[x][y]*ratio)
                        found = 1;break
                    else:
                        for k in d[x]:
                            if k not in seen:
                                stack.append((k,ratio*d[x][k]))
                                seen.add(k)
                if not found: ans.append(-1.0)
        return ans
