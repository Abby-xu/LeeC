class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def is_sub(str_x, str_y):
            index_x = 0
            index_y = 0
            while index_x < len(str_x) and index_y < len(str_y):
                if str_x[index_x] == str_y[index_y]:
                    index_x += 1
                index_y += 1
            return index_x == len(str_x)
        
        freqs = Counter(strs)
        check_list = []
        words = []
        for string in freqs:
            if freqs[string] > 1:
                check_list.append(string)
            else:
                words.append(string)
        words.sort(key=len, reverse=True)
        for word in words:
            sub = False
            for check in check_list:
                print(check,word)
                if is_sub(word, check):
                    sub = True
                    break
            if not sub:
                return len(word)
        return -1
