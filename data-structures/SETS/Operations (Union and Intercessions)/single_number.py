# Scenario Interview Question for the Financial Sector
# Problem Statement
# You are working as a software engineer for a financial technology company that provides investment portfolio management services. The company is implementing a feature to identify unique transactions in a trading platform. Each trade is recorded with an ID that is unique within a session. However, due to a system glitch, some trades might have been recorded twice.
#
# Your task is to develop a solution to identify the unique trade ID from a list where every trade ID appears exactly twice except for one trade ID which appears only once.
#
# Note:
#
# You must implement a solution with linear runtime complexity, i.e., O(n).
# You should use only constant extra space, i.e., O(1).
# Requirements
# Implement a Python function:
#
# Function Signature: def findUniqueTrade(trade_ids: List[int]) -> int:
# Input:
# A list of integers trade_ids representing trade IDs. Each ID appears exactly twice except for one unique ID which appears only once.
# Output:
# An integer representing the unique trade ID.
# Constraints:
#
# 1 <= len(trade_ids) <= 30,000
# -30,000 <= trade_ids[i] <= 30,000
# Each trade ID in the list appears twice except for one unique trade ID.
# Example Cases:
#
# Example 1:

# trade_ids = [101, 102, 101]
# print(findUniqueTrade(trade_ids))  # Output: 102
# Example 2:

# trade_ids = [200, 300, 200, 400, 300]
# print(findUniqueTrade(trade_ids))  # Output: 400
# Example 3:

# trade_ids = [999]
# print(findUniqueTrade(trade_ids))  # Output: 999

from typing import List


class Solution:
    def findUniqueTradeUsingSet(self, trade_ids: List[int]) -> int:
        """
        Find the unique trade ID in a list where every trade ID appears exactly twice except for one unique ID.

        This approach uses a set to keep track of trade IDs. If a trade ID appears twice, it is removed from the set;
        otherwise, it is added. At the end, the set contains only the unique trade ID.

        Parameters:
        trade_ids (List[int]): A list of integers representing trade IDs. Each ID appears exactly twice except for one
                               unique ID which appears only once.

        Returns:
        int: The unique trade ID.

        Example:
        >>> solution = Solution()
        >>> solution.findUniqueTradeUsingSet([101, 102, 101])
        102

        >>> solution.findUniqueTradeUsingSet([200, 300, 200, 400, 300])
        400

        >>> solution.findUniqueTradeUsingSet([999])
        999

        Constraints:
        - 1 <= len(trade_ids) <= 30,000
        - -30,000 <= trade_ids[i] <= 30,000
        - Each trade ID in the list appears twice except for one unique trade ID.
        """
        unique_ids_set = set()

        for trade_id in trade_ids:
            if trade_id in unique_ids_set:
                unique_ids_set.remove(trade_id)
            else:
                unique_ids_set.add(trade_id)

        return unique_ids_set.pop()

    def findUniqueTradeUsingXOR(self, trade_ids: List[int]) -> int:
        """
        Find the unique trade ID in a list where every trade ID appears exactly twice except for one unique ID.

        This approach uses the XOR bitwise operation. XOR-ing all trade IDs together will cancel out those that appear twice,
        leaving only the unique trade ID.

        Parameters:
        trade_ids (List[int]): A list of integers representing trade IDs. Each ID appears exactly twice except for one
                               unique ID which appears only once.

        Returns:
        int: The unique trade ID.

        Example:
        >>> solution = Solution()
        >>> solution.findUniqueTradeUsingXOR([101, 102, 101])
        102

        >>> solution.findUniqueTradeUsingXOR([200, 300, 200, 400, 300])
        400

        >>> solution.findUniqueTradeUsingXOR([999])
        999

        Constraints:
        - 1 <= len(trade_ids) <= 30,000
        - -30,000 <= trade_ids[i] <= 30,000
        - Each trade ID in the list appears twice except for one unique trade ID.
        """
        unique_trade_id = 0

        for trade_id in trade_ids:
            unique_trade_id ^= trade_id

        return unique_trade_id
