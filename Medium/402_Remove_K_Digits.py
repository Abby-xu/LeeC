class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i, d in enumerate(num):
            while stack and k > 0 and stack[-1] > d:
                k -= 1
                stack.pop()
            stack.append(d)
        for i in range(k):
            stack.pop()
        num = ''.join(stack).lstrip('0')
        return num if num else '0'
