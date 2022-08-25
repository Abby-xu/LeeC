class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(char) <= magazine.count(char) for char in set(ransomNote))