## Write a Python program to remove the nth index character from a nonempty string.

import numpy as np

s = np.array(list(input("Enter a string: ")))
index = int(input("Enter index to be removed: "))
if index>=len(s):
    print("index out of range")
else:
    s = np.delete(s, index)
    result = ""
    for i in s:
        result += i
    print(s,result)