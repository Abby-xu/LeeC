class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        if len(pattern) != len(s_list): return False
        
        return (len(set(pattern)) == len(set(s_list)) == len(set(zip(pattern, s_list))))
