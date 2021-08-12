class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        new_dict = Counter(arr)
        for num in sorted(arr, key = abs):
            if new_dict[num] > 0 and new_dict[num * 2] > 0:
                new_dict[num] -= 1
                new_dict[num * 2] -= 1
        for freq in new_dict.values():
            if freq > 0: return False
        return True