class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        
        def dfs(curr, nums):                          
            out.append(curr[:]) 
            for i in range(len(nums)):
                if i > 0 and nums[i-1] == nums[i]:     
                    continue
                dfs(curr+[nums[i]], nums[i+1:])      
                
        dfs([],nums)                             
        return out