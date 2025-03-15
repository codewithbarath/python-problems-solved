class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        sentence1="".join(word1)
        sentence2="".join(word2)

        if sentence1==sentence2:
            return "true"
        return "flase"
c1=Solution()
print(c1.arrayStringsAreEqual(["ab","c"],["a","bc"]))
