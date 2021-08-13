class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        str_dict = {}
        for i in strs:
            s = str(sorted(i))
            if s in str_dict.keys(): str_dict[s].append(i)
            else: str_dict[s] = [i]
        return list(str_dict.values())