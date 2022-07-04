class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left2right = [1] * n
        right2left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1]+1
        for i in reversed(range(n-1)):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1]+1
        return sum(map(max, zip(left2right, right2left)))