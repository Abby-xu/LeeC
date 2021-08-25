class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        mark_num1 = num1.index('+')
        mark_num2 = num2.index('+')
        real_num1, imag_num1 = int(num1[:mark_num1]), int(num1[mark_num1+1:-1])
        real_num2, imag_num2 = int(num2[:mark_num2]), int(num2[mark_num2+1:-1])
        real_out = real_num1*real_num2-imag_num1*imag_num2
        imag_out = real_num1*imag_num2+real_num2*imag_num1
        return str(real_out) + '+' + str(imag_out) + 'i' 
