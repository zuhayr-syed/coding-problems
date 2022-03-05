class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for number in nums:
            if (number in dictionary):
                return True
            else:
                dictionary[number] = 1
        return False