#-----------------------------------------------------------------------------
# Runtime: 36ms
# Memory Usage: 
# Link: 
#-----------------------------------------------------------------------------

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random

class Solution:
    def findSecretWord(self, wordlist: [str], master: 'Master') -> None:
        wordlistHashSet = tuple(set(wordlist))

        for _ in range(10):
            word = random.choice(wordlistHashSet)

            result = master.guess(word)
            if result == len(word):
                break

            wordlistHashSet = [ anotherWord for anotherWord in wordlistHashSet if self.__matchCount(word, anotherWord) == result]

    def __matchCount(self, word1: str, word2: str) -> int:
        count = 0
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
        return count

class Master:

    def __init__(self, secret: str, wordlist: [str]):
        self.secret = secret
        self.wordlist = set(wordlist)
        self.guessCount = 0

    def guess(self, word: str) -> int:
        self.guessCount += 1

        if len(self.secret) != len(word):
            return -1
        if word not in self.wordlist:
            return -1

        count = 0
        for i in range(len(word)):
            if word[i] == self.secret[i]:
                count += 1

        return count
