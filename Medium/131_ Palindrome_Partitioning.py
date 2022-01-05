class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(p):
            return p == p[::-1]
        
        d = defaultdict(list)

        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if is_palindrome(s[i:j]):
                    d[i].append(j)

        path = []

        def dfs(u):
            if u == len(s):
                yield path[:]
            else:
                for v in d[u]:
                    path.append(s[u:v])
                    yield from dfs(v)
                    path.pop()

        return list(dfs(0))
