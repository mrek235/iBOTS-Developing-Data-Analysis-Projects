import numpy as np
import sys

inp = sys.argv[1]
out = sys.argv[2]

arr = np.load(inp,allow_pickle=True)
std_array = arr-arr.mean()/arr.std()
np.save(out,std_array)