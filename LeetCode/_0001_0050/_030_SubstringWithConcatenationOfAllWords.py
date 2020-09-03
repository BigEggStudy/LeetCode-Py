#-----------------------------------------------------------------------------
# Runtime: 56ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def findSubstring(self, s: str, words: list):
        if len(words) == 0:
            return words

        word_dic = {}
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1

        word_length = len(words[0])
        result = []
        for i in range(word_length):
            left = i
            temp_dic = {}
            for j in range(i, len(s) - word_length + 1, word_length):
                current_word = s[j:j + word_length]
                if current_word not in word_dic:
                    left = j + word_length
                    temp_dic = {}
                    continue

                if current_word in temp_dic:
                    temp_dic[current_word] += 1
                else:
                    temp_dic[current_word] = 1

                while temp_dic[current_word] > word_dic[current_word]:
                    temp_dic[s[left:left + word_length]] -= 1
                    left += word_length

                if temp_dic == word_dic:
                    result.append(left)

        return result
