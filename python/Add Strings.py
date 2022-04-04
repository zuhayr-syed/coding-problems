class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = 0
        result += self.stringSum(num1)
        result += self.stringSum(num2)
        return str(result)       
    
    def stringSum(self, string) -> int:
        dict={'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9': 9, '0':0}
        mult = 1
        icr = len(string) - 1
        result = 0
        while (icr >= 0):
            result += dict[string[icr]] * mult
            icr -= 1
            mult *= 10
        return result