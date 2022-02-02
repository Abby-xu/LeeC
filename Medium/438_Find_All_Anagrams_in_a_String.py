class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count1 = collections.Counter(p)
        count2 = collections.Counter(s[:len(p)])
        i, j = 0, len(p)
        size = len(s)
        ans = []
        while j <= size:
            if count2 == count1:
                ans += i,
            if j < size:
                count2[s[j]] += 1
            count2[s[i]] -= 1
            if count2[s[i]]==0:
                del count2[s[i]]
            i += 1
            j += 1
        return ans
