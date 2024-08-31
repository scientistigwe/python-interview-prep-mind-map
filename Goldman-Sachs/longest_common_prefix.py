# Scenario: Autocomplete Feature in a Search Engine (LeetCode: #14. Longest Common Prefix)
# Imagine you are working on an autocomplete feature for a search engine.
# When users start typing a query, the system should suggest the most relevant completions.
# To optimize this feature, the system needs to determine the longest common prefix among all potential search terms
# that match the user's input so far.
# For instance, if the user has typed "flo", and the matching terms are ["flower", "flow", "flight"],
# the autocomplete system should suggest "flo" as the common prefix.
# In case there is no common prefix, the system should not suggest anything.

# Problem Statement:
# Given a list of strings, find the longest common prefix among them.
# If there is no common prefix, return an empty string.

# Example Usage:
# Example 1:
# Input: ["flower", "flow", "flight"]
# Output: "fl"
# Explanation: The longest common prefix for all three strings is "fl".

# Example 2:
# Input: ["dog", "racecar", "car"]
# Output: ""
# Explanation: There is no common prefix among these strings, so the output is an empty string.

# Example 3:
# Input: ["flower", "flow", "right"]
# Output: ""
# Explanation: There is no common prefix among these strings.

# Constraints:
# - The array length is between 1 and 200.
# - Each string's length is between 0 and 200.
# - All strings consist of only lowercase English letters.

class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        # Edge case: if the list is empty, return an empty string
        if not strs:
            return ""

        # Start with the first string as the initial prefix
        prefix = strs[0]

        # Iterate through each string in the list
        for string in strs:
            # Adjust the prefix until it matches the beginning of the string
            while string[:len(prefix)] != prefix:
                # Trim the prefix by one character from the end
                prefix = prefix[:-1]
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""

        # Return the longest common prefix found
        return prefix


# Example Usage:
solution = Solution()

# Test case 1
print(solution.longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"

# Test case 2
print(solution.longest_common_prefix(["dog", "racecar", "car"]))  # Output: ""

# Test case 3
print(solution.longest_common_prefix(["flower", "flow", "right"]))  # Output: ""

# Complexity Analysis:
# Time Complexity: O(S), where S is the sum of all characters in all strings.
# - In the worst case, every character in every string needs to be compared, making this approach linear with respect to the total number of characters.
# Space Complexity: O(1)
# - The solution uses a constant amount of extra space, regardless of the input size.

# Follow-up Questions:
# 1. What if the input list contains only one string?
# - The function would return that string itself as the longest common prefix.
#
# 2. How would you handle the case where the input strings are extremely large?
# - For large strings, the function would still work efficiently because it only compares characters up to the length of the shortest string. However, in cases where memory or performance is critical, further optimizations might be needed.
#
# 3. Can this solution be optimized further?
# - One possible optimization could be to start by finding the shortest string in the list, since the longest possible prefix cannot be longer than the shortest string. This could reduce unnecessary comparisons.
#
# 4. How would you modify the algorithm if the input strings are in a stream (i.e., you cannot access all strings at once)?
# - In a streaming scenario, you could maintain the current longest common prefix and update it as new strings arrive. This would require adjusting the prefix dynamically as more data is processed.
