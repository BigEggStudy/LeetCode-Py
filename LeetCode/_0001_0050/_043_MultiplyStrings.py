#-----------------------------------------------------------------------------
# Runtime: 84ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        len_num1 = len(num1)
        len_num2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        result_list = [0] * 220

        dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        for i in range(len_num1):
            for j in range(len_num2):
                result_list[i + j] += dic[num1[i]] * dic[num2[j]]

        carry = 0
        result = ""
        for i in range(len_num1 + len_num2):
            carry, rest = divmod(result_list[i] + carry, 10)
            result = str(rest) + result

        for i, ch in enumerate(result):
            if ch != '0':
                break

        return result[i:]
