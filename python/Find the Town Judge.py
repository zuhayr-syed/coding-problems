class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0] * (n + 1)
        for x,y in trust:
            count[x] -= 1
            count[y] += 1
        for index in range(1, len(count)):
            if (count[index] == n - 1):
                return index
        return -1