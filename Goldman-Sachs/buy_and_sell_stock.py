# Scenario: Stock Trading Profit Calculation (leetcode: #121. Best Time to Buy and Sell Stock)
#
# Imagine you are working for a financial analysis company that needs to determine the maximum profit
# that can be achieved by buying and selling a stock exactly once. Given a list of stock prices
# where each element represents the price of the stock on a given day, you need to write a function
# to compute the maximum profit. The function should return the maximum profit achievable by buying
# on one day and selling on a later day. If no profit is possible, the function should return 0.
#
# Example Usage:
# - Input: [7, 1, 5, 3, 6, 4]
#   Output: 5
#   Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.
#
# - Input: [7, 6, 4, 3, 1]
#   Output: 0
#   Explanation: No transactions can be made that will result in profit.
#
# Complexity Analysis:
# - Time Complexity: O(n), where n is the number of days.
#   - We make a single pass through the list to determine the minimum price and calculate the profit.
# - Space Complexity: O(1), as we only use a few variables to keep track of the minimum price and maximum profit.

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize variables to keep track of the minimum price and maximum profit
        min_price = float('inf')
        max_profit = 0

        # Iterate over each price in the list
        for price in prices:
            # Update min_price if a lower price is found
            if price < min_price:
                min_price = price
            # Calculate profit if selling at the current price
            profit = price - min_price
            # Update max_profit if a higher profit is found
            if profit > max_profit:
                max_profit = profit

        # Return the maximum profit found
        return max_profit


# Example usage:
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
print(solution.maxProfit(prices1))  # Output: 5

prices2 = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices2))  # Output: 0
