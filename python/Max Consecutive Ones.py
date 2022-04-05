class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxOnes = 0
        for number in nums:
            if number == 1:
                counter += 1
            else:
                if counter > maxOnes:
                    maxOnes = counter
                counter = 0
        if counter > maxOnes:
            maxOnes = counter
        return maxOnes