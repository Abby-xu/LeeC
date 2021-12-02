class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, len(nums)-1 # three pointers
        while white <= blue:
            if nums[white] == 0: # [red] swap red and white
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else: # [blue] swap white and blue
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
