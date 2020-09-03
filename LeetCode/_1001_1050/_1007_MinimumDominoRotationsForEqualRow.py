#-----------------------------------------------------------------------------
# Runtime: 1248ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def minDominoRotations(self, A: [int], B: [int]) -> int:

        def check(num: int) -> int:
            rotation_a = rotation_b = 0
            for i in range(len(A)):
                if A[i] != num and B[i] != num:
                    return -1
                elif A[i] != num:
                    rotation_a += 1
                elif B[i] != num:
                    rotation_b += 1
            return min(rotation_a, rotation_b)

        rotation = check(A[0])
        if rotation != -1 or A[0] == B[0]:
            return rotation
        else:
            return check(B[0])
