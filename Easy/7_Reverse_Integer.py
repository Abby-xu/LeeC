class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31-1 or x == 0 or x < -2**31: return 0
        out = '-' if x < 0 else ''
        x_list = [int(i) for i in str(abs(x))]
        x_list.reverse()
        for j in x_list: out += str(j)
        return int(out) if int(out) < 2**31-1 and int(out) > -2**31 else 0
