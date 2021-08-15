class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False
        par = {')':'(', ']':'[', '}':'{'}
        stack = []
        for i in range(len(s)):
            if s[i] in [')', ']', '}']:
                if len(stack) == 0:
                    return False
                elif stack.pop() != par[s[i]]:
                    return False
            else:
                stack.append(s[i])
        return stack == []