#-----------------------------------------------------------------------------
# Runtime: 108ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        res = {}
        for i in strs:
            s = ''.join(sorted(i))
            res[s] = res.get(s,[])+[i]

        return list(res.values())

    def groupAnagrams_linear(self, strs: [str]) -> [[str]]:
        dic = {}
        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            if key in dic:
                dic[key].append(word)
            else:
                dic[key] = [word]

        return list(dic.values())
