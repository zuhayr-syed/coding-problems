class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[dup]:
                dup += 1
                nums[dup] = nums[i]
        dup += 1
                
        return dup