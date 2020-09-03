#-----------------------------------------------------------------------------
# Runtime: 32ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

class Solution:
    def fullJustify(self, words: [str], maxWidth: int) -> [str]:
        result = []
        start_index, current_length = 0, 0

        for i in range(len(words)):
            if current_length + len(words[i]) > maxWidth:
                space = maxWidth - current_length + (i - start_index)
                new_line = ''
                for j in range(start_index, i):
                    new_line += words[j]

                    space_count = maxWidth - len(new_line) if j == i - 1 else space // (i - start_index - 1) + (1 if (j - start_index < (space % (i - start_index - 1))) else 0)
                    new_line += ' ' * space_count

                result.append(new_line)

                current_length = 0
                start_index = i

            current_length += len(words[i]) + 1

        new_line = ''
        for j in range(start_index, len(words)):
            new_line += words[j]
            space_count = 1 if j != len(words) - 1 else maxWidth - len(new_line)
            new_line += ' ' * space_count
        result.append(new_line)

        return result
