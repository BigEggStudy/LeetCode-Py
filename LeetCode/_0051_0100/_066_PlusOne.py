#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        carry = 0
        digits[-1] += 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry < 10:
                digits[i] += carry
                return digits
            else:
                digits[i] = 0
                carry = 1
        return digits if carry == 0 else [1] + digits
