class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        dic = dict()
        dic[0] = 1
        
        for i in range(len(nums)):
            sums += nums[i]
            count += dic.get(sums - k, 0)
            dic[sums] = dic.get(sums, 0) + 1
        return count
            
