class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0
        for index in range(len(nums)):
            if (nums[index] != 0):
                nums[index], nums[zero] = nums[zero], nums[index]
                zero += 1