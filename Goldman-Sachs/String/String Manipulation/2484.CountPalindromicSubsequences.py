MOD = 10 ** 9 + 7


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        # Array to store prefix counts of digits 0-9
        prefix = [[0] * 10 for _ in range(n)]
        # Array to store suffix counts of digits 0-9
        suffix = [[0] * 10 for _ in range(n)]

        # Fill prefix array
        for i in range(n):
            if i > 0:
                prefix[i] = prefix[i - 1][:]
            prefix[i][int(s[i])] += 1

        # Fill suffix array
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                suffix[i] = suffix[i + 1][:]
            suffix[i][int(s[i])] += 1

        count = 0

        # Iterate over the string to find palindromic subsequences
        for i in range(1, n - 3):
            for j in range(i + 3, n):
                if s[i] == s[j]:
                    # Find the number of palindromic subsequences formed with s[i] and s[j]
                    for d in range(10):
                        if prefix[i - 1][d] > 0 and suffix[j + 1][d] > 0:
                            count = (count + 1) % MOD

        return count


# Example usage:
sol = Solution()
print(sol.countPalindromicSubsequence("103301"))  # Output: 2
print(sol.countPalindromicSubsequence("0000000"))  # Output: 21
print(sol.countPalindromicSubsequence("9999900000"))  # Output: 2
