class Solution:
    def confusingNumber(self, n: int) -> bool:
        dic = {0:0, 1:1, 6:9, 8:8, 9:6}
        # splite the number to digit
        n_str = [i for i in str(n)]
        # reverse the list
        n_str = list(reversed(n_str))
        for i in range(len(n_str)):
            if int(n_str[i]) in dic.keys():
                n_str[i] = str(dic[int(n_str[i])])
            else:
                return False
        out = int("".join(n_str))
        return False if out == n else True

        # htransfer the list to int whil eusing the dic
        # check if == to original
