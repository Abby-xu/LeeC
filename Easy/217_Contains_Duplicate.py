class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        ### hash map ###
        nums_dict = {}
        
        # iterate each num and stor to the dict
        for num in nums:
            
            #check if num already stored
            if num in nums_dict.keys():
                return True
            else:
                nums_dict[num] = 1
                
        return False
        '''
        return not(len(nums) == len(set(nums)))
