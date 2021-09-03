class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        '''
        input: 
        list of words
        char order => size == 26
        output: bool for order
        '''
        # build the alien dic
        dic = {}
        for index, char in enumerate(order):
            dic[char] = index
        
        # go through every word in the list
        for i in range(0,len(words)-1):
            curr, nxt = words[i], words[i+1]
            if_equal = True
            j = 0
            while j < min(len(curr), len(nxt)):
                if dic[curr[j]] < dic[nxt[j]]:
                    if_equal = False
                    break
                elif dic[curr[j]] > dic[nxt[j]]:
                    return False
                else:
                    j += 1
            # edge case for same char order but diff length
            if if_equal:
                if len(nxt) < len(curr):
                    return False
        return True
