#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path or not path.strip():
            return '/'

        path = path.strip('/')
        folders = path.split('/')
        ignore = 0
        result = ''
        for i in range(len(folders) - 1, -1, -1):
            if not folders[i] or folders[i] == '.':
                continue
            if folders[i] == '..':
                ignore += 1
                continue
            if ignore > 0:
                ignore -= 1
                continue

            result = '/' + folders[i] + result

        return result if len(result) > 0 else '/'
