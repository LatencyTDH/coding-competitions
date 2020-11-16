class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word2) < len(word1):
            word1, word2 = word2, word1
        
        word1 = " " + word1
        word2 = " " + word2
        m = len(word1)
        n = len(word2)
        dp = list(range(m))
        if m == 1:
            return n - 1
        for i in range(1, n):
            diag = i - 1
            prev = i
            for j in range(1, m):
                above = dp[j]
                subc = 0 if word1[j] == word2[i] else 1
                dp[j] = min(diag + subc, prev + 1, above + 1)
                diag = above
                prev = dp[j]
        return dp[-1]
    
# if __name__ == "__main__":
#     md = Solution().minDistance
#     assert md("horse", "ros") == 3
#     assert md("", "a") == 1
#     assert md("b", "b") == 0
#     assert md("ab", "b") == 1
#     assert md("intention", "execution") == 5
#     assert md("zoologicoarchaeologist", "zoogeologist") == 10
                
