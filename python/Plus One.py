class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits) - 1] += 1
        for index in range(len(digits) - 1, 0, -1):
            if digits[index] == 10 and index != 0:
                digits[index] = 0
                digits[index - 1] += 1
            else:
                break
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else:
            return digits
            