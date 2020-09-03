#-----------------------------------------------------------------------------
# Runtime: 40ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_length = len(a) - 1
        b_length = len(b) - 1
        carry = 0
        result = ''
        while a_length >= 0 or b_length >= 0:
            a_value = int(a[a_length]) if a_length >= 0 else 0
            b_value = int(b[b_length]) if b_length >= 0 else 0

            sum_value = a_value + b_value + carry
            result = str(sum_value & 1) + result
            carry = sum_value >> 1

            a_length -= 1
            b_length -= 1

        return result if carry == 0 else '1' + result
