import numpy as np
import copy 
a =[1,2,3]
t = copy.deepcopy(a)
t1 = a

a = [3]
print(t)
print(t1)


rain = list(range(100))
evap = np.zeros_like(rain) + 0.2
print(evap)
