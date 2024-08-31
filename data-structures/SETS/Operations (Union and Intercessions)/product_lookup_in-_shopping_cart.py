# Imagine you're working as a software engineer at an e-commerce company. Your team is developing a feature that allows
# customers to search for specific products within their shopping cart before proceeding to checkout.
# The shopping cart can contain a variety of items, but customers often add and remove items frequently.
#
# To enhance the user experience, the system needs to efficiently check if a particular product
# (identified by a unique product ID) is present in the user's shopping cart before adding it again or removing it.

class Solution:
    def product_lookup(self, arr: list, product:str) -> bool:
        return product in set(arr)

solution = Solution()
print(solution.product_lookup(['prod1','prod2','prod3'], 'prod2'))
print(solution.product_lookup(['prod1','prod2','prod3'], 'prodX'))