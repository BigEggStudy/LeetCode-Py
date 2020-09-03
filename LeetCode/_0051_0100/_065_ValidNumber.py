#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        n = s.strip()
        if not n:
            return False
        return re.match(r"^([+-]{0,1}(([0-9]+){1}[.]{0,1}([0-9]+){0,1}|([.][0-9]+){1})([e][+|-]{0,1}[0-9]+){0,1})$", n) is not None
