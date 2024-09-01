# Leetcode: #647. Palindromic Substrings
class Solution:
    def countSubstring(self, s: str) -> int:
        # Get the length of the string
        n = len(s)

        # Initialize a counter to keep track of the number of palindromic substrings
        count = 0

        # This helper function will expand around the center of a possible palindrome
        def expandAroundCentre(left: int, right: int):
            # We use 'nonlocal' to allow modification of the 'count' variable outside of this scope
            nonlocal count

            # Expand as long as we're within bounds and the characters match
            while left >= 0 and right < n and s[left] == s[right]:
                # Found a palindrome, so increment the count
                count += 1

                # Expand outwards: move left pointer to the left, right pointer to the right
                left -= 1
                right += 1

        # Iterate through each character and gap in the string
        for i in range(n):
            # Consider odd-length palindromes centered at each character
            expandAroundCentre(i, i)

            # Consider even-length palindromes centered between each pair of characters
            expandAroundCentre(i, i + 1)

        # Return the total count of palindromic substrings found
        return count


# Real-world Scenario:
# Imagine you're working at a software company developing a text editor that highlights palindromic substrings
# as part of an educational tool to help students understand palindromes.

# You have a test string to analyze:
s = "xabay"

# Instantiate the solution class
solution = Solution()

# Use the countSubstring method to determine the number of palindromic substrings in the test string
print(solution.countSubstring(s))  # Expected Output: 6

# --- Questions and Answers Section ---

# Q1: What is the expected output and why?
# A1: The expected output is 6. The palindromic substrings in the string "abcaa" are:
# "a" (3 times), "b", "c", and "aa". These add up to 6 palindromic substrings.

# Q2: How does the expandAroundCentre function work?
# A2: This function takes two indices (left and right) and expands outwards to check for palindromic
# substrings centered at those indices. If the characters at the current left and right indices are
# the same, it's a palindrome, so we increase the count and continue expanding. We stop when the characters
# no longer match or when the indices go out of bounds.

# Q3: Why do we have two calls to expandAroundCentre in the loop?
# A3: The first call handles palindromes of odd length, where the palindrome has a single character at the center.
# The second call handles even-length palindromes, where the center is between two characters. This ensures we
# capture all possible palindromic substrings.

# Q4: Can this method handle strings of any length?
# A4: Yes, the method is designed to work efficiently for strings of up to 1000 characters, as specified by
# the problem constraints. The time complexity is O(n^2), which is manageable for the given input limits.
