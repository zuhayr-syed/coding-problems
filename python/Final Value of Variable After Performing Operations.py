class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0
        for index in operations:
            if('+' in index):
                counter += 1
            else:
                counter -= 1
        return counter