class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index in range(len(nums)):
            num2 = target - nums[index]
            if(num2 in dictionary):
                return [dictionary[num2], index]
            else:
                dictionary[nums[index]] = index