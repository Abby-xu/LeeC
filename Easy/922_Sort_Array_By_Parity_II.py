class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if (nums[i]%2 == i%2):
                continue
            else:
                j = 1
                while nums[i]%2 != i%2:
                    temp = nums[i+j]
                    nums[i+j] = nums[i]
                    nums[i] = temp
                    j += 1
        return nums
