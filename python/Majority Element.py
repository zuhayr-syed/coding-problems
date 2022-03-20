class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        
        for number in nums:
            if number in dict:
                dict[number] += 1
            else:
                dict[number] = 1
        
        for number in nums:
            if dict[number] >= len(nums)/2:
                return number

# O(1) space
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = nums[0]
        counter = 1
        
        for number in nums:
            if number == maj:
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                maj = number
                counter = 1
        
        return maj