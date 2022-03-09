class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for number in range(1, n + 1):
            divFive = number % 5 == 0
            divThree = number % 3 == 0
            if (divThree and divFive):
                answer.append("FizzBuzz")
            elif (divThree):
                answer.append("Fizz")
            elif (divFive):
                answer.append("Buzz")
            else:
                answer.append(str(number))
        return answer