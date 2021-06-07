## Take a binary input form user and segregate all 1's to left side and 0's to right side.
# Ex: Input : 1010011 Output : 111100

import numpy as np

arr = np.array(list(input("Enter the binary number : ")))
arr = np.sort(arr)[::-1]
result = ""
for i in arr:
    result += i
print(result)
