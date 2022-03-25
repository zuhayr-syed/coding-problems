class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        icr = 1
        numTotal = 0
        while (icr <= len(nums)):
            numTotal += icr
            icr += 1
         
        for number in nums:
            numTotal -= number
        
        return numTotal