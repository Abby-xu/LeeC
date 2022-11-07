class Solution:
    def maximum69Number (self, num: int) -> int:
        num_s = str(num)
        for idx,char in enumerate(num_s):
            if char == '6': return int(num_s[:idx]+'9'+num_s[idx+1:])
        return num
