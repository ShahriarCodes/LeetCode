class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        lst = sentence.split()
        for i in range (len(lst)):
            word = lst[i]
            if len(word) >= len(searchWord):
                if word[:len(searchWord)] == searchWord:
                    return i + 1
        return -1
                    
