
import numpy as np


# making an arrays of zeroes

zero_arrays = np.zeros(3)

zero_arrays_2d = np.zeros((3,4))

print(zero_arrays,"\n",zero_arrays_2d)

# making ones arrays

one_arrays=np.ones(3)
print(one_arrays)

one_arrays = np.ones((4,5))
print(one_arrays)

# creating empty arrays

empty_arrays = np.empty((5,5))
print(empty_arrays)

#creating diagonal arrays...

diag_arrays = np.eye(5,8)
print(diag_arrays)


#creating a range arrays....

range_ararys =np.arange((4))
print(range_ararys)

#creating a arrays using linspace and provide gap between the numbers

line_gap = np.linspace(0,20,5)
print(line_gap)