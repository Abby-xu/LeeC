from typing import List

##### 8/1/2021 #####
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

##### 8/2/2021 #####
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        wanted = {}
        for i in range(len(nums)):
            if target - nums[i] not in wanted:
                wanted[nums[i]] = i
            else:
                return [wanted[target - nums[i]], i]

### test ###
nums = [1,2,3,4,5,6,7,8,9,10]
target = 8

s = Solution()
print(s.twoSum(nums,target))