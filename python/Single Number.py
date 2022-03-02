class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}
        for integer in nums:
            if (integer in dictionary):
                dictionary[integer] += 1
            else:
                dictionary[integer] = 1
        for integer in nums:
            if (dictionary[integer] == 1):
                return integer
        