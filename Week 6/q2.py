##Find cubic root of 27, 64, 891 using sciPy special package.

import numpy as np
from scipy.special import cbrt

nums = [27, 64, 891]
nums_root = cbrt(nums)        

print(nums_root)