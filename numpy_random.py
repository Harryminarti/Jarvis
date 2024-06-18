
import numpy as np

# generating random number ...........

var1 = np.random.rand(5) # creating an arrays of random positive number beteween 0 to 1 in point

var2 = np.random.randn(5) # creating an arrays of random negative number

print(var1,"\n",var2)

var3 = np.random.ranf(5) # creating an arrays of random number between 0 to 1

print(var3)

var4 = np.random.randint(1,55,8) # creating an random number arrays of size 8 between the 1 to 55

print(var4)