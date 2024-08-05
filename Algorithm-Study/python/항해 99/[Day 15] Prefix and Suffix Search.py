# LeetCode Prefix and Suffix Search https://leetcode.com/problems/prefix-and-suffix-search/description/

class WordFilter:

    def __init__(self, words: List[str]):
        self.dict = {}
        for index, word in enumerate(words):
            length = len(word)
            for i in range(length + 1):  
                for j in range(length + 1):  
                    prefix = word[:i]
                    suffix = word[-j:] if j != 0 else ''
                    self.dict[(prefix, suffix)] = index

    def f(self, pref: str, suff: str) -> int:
        return self.dict.get((pref, suff), -1)