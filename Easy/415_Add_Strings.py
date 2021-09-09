class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
#         return str(int(num1)+int(num2))

        i, j, carry = len(num1)-1, len(num2)-1, 0
        out = []
        while i >= 0 or j >= 0 or carry > 0:
            n1, n2 = 0, 0
            if i >= 0:
                n1 = int(num1[i])
                i -= 1
            if j >= 0:
                n2 = int(num2[j])
                j -= 1
            sums = n1 + n2 + carry
            carry = 1 if sums >= 10 else 0
            out.insert(0, str(sums%10))
        return ''.join(out)
