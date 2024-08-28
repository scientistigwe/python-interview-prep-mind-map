#
# Scenario: Financial Sector Investment Overlap
# Imagine you're a financial analyst working at a large investment firm.
# You have access to two different clients' lists of preferred investment options.
# Each list represents a client's top investment choices, ranked by preference.
# Your task is to identify the investment options that both clients agree on, and among those,
# determine which ones have the highest combined priority, i.e., the lowest sum of their rankings on both lists.
#
# In this scenario, each investment option's ranking is critical because it reflects how strongly a client prefers that investment.
# Your goal is to find the investments with the smallest sum of their rankings from both clients' lists.
#
# Example Scenario
# Client A's Preferred Investments:
# List A: ["Real Estate", "Stocks", "Bonds", "Mutual Funds"]
# Client B's Preferred Investments:
# List B: ["Cryptocurrency", "Bonds", "Real Estate", "Stocks"]
# In this case, "Real Estate" appears at index 0 in Client A's list and index 2 in Client B's list,
# for a combined index sum of 2. "Stocks" and "Bonds" also appear in both lists, but "Real Estate" has the lowest index sum,
# indicating it’s the most mutually prioritized investment.

import sys


class FindMutualInvestment:

    def minimum_sum_of_common_investment(self, list1: list, list2: list) -> list:
        """
        Finds the common investments between two lists with the minimum index sum.

        Complexity Analysis:

        Time Complexity:
        - Building the `index_map` dictionary: O(n), where n is the length of list1.
        - Iterating through `list2`: O(m * n), where m is the length of list2.
          - This is due to the `list1.index()` operation, which is O(n) for each element in list2.
        - Sorting the `common_investment` list: O(k * log k), where k is the number of common investments.
        - Overall Time Complexity: O(m * n).

        Space Complexity:
        - `index_map` dictionary: O(n) space, where n is the length of list1.
        - `common_investment` list: O(m) space in the worst case, where m is the length of list2.
        - Overall Space Complexity: O(n + m).

        :param list1: List of investment options from the first source.
        :param list2: List of investment options from the second source.
        :return: Sorted list of common investments with the minimum index sum.
        """
        self.list1 = list1
        self.list2 = list2

        index_map = {investment: index for index, investment in enumerate(self.list1)}
        common_investment = []
        min_sum = sys.maxsize

        for i, investment in enumerate(list2):
            if investment in index_map:
                j = list1.index(investment)
                current_sum = i + j
                if current_sum < min_sum:
                    min_sum = current_sum
                    common_investment = [investment]
                elif current_sum == min_sum:
                    common_investment.append(investment)

        return sorted(common_investment)


# Example usage
minimum_sum_func = FindMutualInvestment()

ListA = ["Real Estate", "Stocks", "Bonds", "Mutual Funds"]
ListB = ["Cryptocurrency", "Bonds", "Real Estate", "Stocks"]
result = minimum_sum_func.minimum_sum_of_common_investment(ListA, ListB)
print(result)  # Expected Output: ["Real Estate"]



