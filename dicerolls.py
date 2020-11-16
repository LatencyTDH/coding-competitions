class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = (10 ** 9) + 7
        if target < d or f*d < target:
            return 0
        size = max(f+1, target + 1)
        dp = [0] * size
        for face in range(1, f+1):
            dp[face] = 1
        
        for roll in range(d-1):
            new_dp = [0] * size
            for total in range(1, min((roll + 2) * f + 1, target + 1)):
                for face_val in range(1, f+1):
                    if total - face_val > 0 and dp[total - face_val] > 0:
                        new_dp[total] += dp[total - face_val]
            dp = new_dp
        return dp[target] % MOD
