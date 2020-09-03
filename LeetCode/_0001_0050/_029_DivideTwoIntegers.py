#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

INT_MAX = 2 ** 31 - 1

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0 or divisor == 1:
            return dividend
        if divisor == -1:
            return -dividend if -dividend < INT_MAX else INT_MAX

        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        step_divisor = divisor
        step_result = 1
        while dividend >= step_divisor + step_divisor:
            step_divisor += step_divisor
            step_result += step_result

        while dividend >= divisor:
            if dividend >= step_divisor:
                dividend -= step_divisor
                result += step_result
            step_divisor = (step_divisor >> 1)
            step_result = (step_result >> 1)

        return sign * result
