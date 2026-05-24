from utils.parity import *

# Check if a number is even
print(parity_of_number(10))  # True (even) | False (odd)

# Filter a list by parity
print(parity_of_list([10, 11, 12], "even"))  # [10, 12]
print(parity_of_list([10, 11, 12], "odd"))   # [11]

# Count even and odd numbers
print(count_of_elements([9, 8, 18], "even"))  # 2
print(count_of_elements([9, 8, 18], "odd"))   # 1
print(count_of_elements([9, 8, 18]))          # (2, 1) - tuple