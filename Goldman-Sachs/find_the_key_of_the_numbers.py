# Scenario: Generating a Unique Key from Multiple Numeric Codes
#
# In a cataloging system, you need to generate a unique key from three given numbers. Each number should
# be treated as a four-digit number by padding with leading zeros if necessary. The unique key is formed
# by taking the smallest digit from each position across the three numbers. For example, given three numbers,
# you need to pad them to four digits, then find the smallest digit in each position to form the key.
#
# Example Usage:
# - Input: num1 = 1, num2 = 10, num3 = 1000
#   Output: 0
#   Explanation: After padding, the numbers are "0001", "0010", and "1000". The key is formed by taking
#   the smallest digit in each position: "0000".
#
# - Input: num1 = 987, num2 = 879, num3 = 798
#   Output: 777
#   Explanation: After padding, the numbers are "0987", "0879", and "0798". The key is formed by taking
#   the smallest digit in each position: "0777".
#
# - Input: num1 = 1, num2 = 2, num3 = 3
#   Output: 1
#   Explanation: After padding, the numbers are "0001", "0002", and "0003". The key is formed by taking
#   the smallest digit in each position: "0001".

def find_key(num1: int, num2: int, num3: int) -> int:
    # Convert numbers to four-digit strings with leading zeros
    str1 = f"{num1:04d}"
    str2 = f"{num2:04d}"
    str3 = f"{num3:04d}"

    # Initialize the key as an empty string
    key = ""

    # Find the smallest digit at each position
    for i in range(4):
        # Get the digit at position i for each number
        digits = [str1[i], str2[i], str3[i]]
        # Find the smallest digit among the three
        min_digit = min(digits)
        # Append the smallest digit to the key
        key += min_digit

    # Convert the key to an integer to remove leading zeros
    return int(key)


# Example usage:
print(find_key(1, 10, 1000))  # Output: 0
print(find_key(987, 879, 798))  # Output: 777
print(find_key(1, 2, 3))  # Output: 1
