#-----------------------------------------------------------------------------
# Runtime: 60ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        len_s, len_p = len(s), len(p)
        last_star_pos_s = -1
        last_star_pos_p = -1

        while i < len_s:
            if j < len_p and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < len_p and p[j] == '*':
                last_star_pos_p = j
                last_star_pos_s = i
                j += 1
                if j == len_p:
                    return True
            else:
                if last_star_pos_s == -1:
                    return False

                last_star_pos_s += 1
                i = last_star_pos_s
                j = last_star_pos_p

        while j < len_p and p[j] == '*':
            j += 1

        return j == len_p and i == len_s
