"""
Scenario: Financial Sector - Finding Common Investments Between Two Portfolios

Problem:
You are given two lists of financial instruments representing two different investment portfolios.
Each list contains the stock tickers of the investments in the respective portfolio.
Your task is to find the common investments between these two portfolios.
The result should contain only the unique stock tickers that are present in both portfolios.

Example 1:
Input:
    portfolio1 = ["AAPL", "GOOGL", "GOOGL", "MSFT"]
    portfolio2 = ["GOOGL", "MSFT"]
Output:
    ["GOOGL", "MSFT"]

Example 2:
Input:
    portfolio1 = ["TSLA", "AMZN", "FB", "NVDA"]
    portfolio2 = ["NVDA", "AAPL", "GOOGL"]
Output:
    ["NVDA"]

Complexity Analysis:
- Time Complexity: O(n + m), where n is the length of `portfolio1` and m is the length of `portfolio2`.
  The reason for this is that creating the sets from the two portfolios takes O(n) and O(m) time respectively,
  and checking for the intersection of these sets takes O(min(n, m)) time.
- Space Complexity: O(n + m) for storing the two sets created from the input lists.
"""

class Solution:
    def intersection(self, portfolio1: list[str], portfolio2: list[str]) -> list[str]:
        set1 = set(portfolio1)
        set2 = set(portfolio2)
        intersection = []

        for stock in set1:
            if stock in set2:
                intersection.append(stock)

        return intersection


# Example usage:
portfolio1 = ["AAPL", "GOOGL", "GOOGL", "MSFT"]
portfolio2 = ["GOOGL", "MSFT"]
solution = Solution()
result = solution.intersection(portfolio1, portfolio2)
print(result)  # Output: ["GOOGL", "MSFT"]
