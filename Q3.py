import numpy as np
from matplotlib import pyplot as plt

x1 = np.random.random(500)

x2 = x1 + 5

x = np.append(x1, x2)

plt.hist(x, 10, density=True)
plt.title("NYU AI School")
plt.show()

def data_mean(x):
   
   return sum(x) / len(x)

def data_variance(x):
   
   return sum((i - data_mean(x)) ** 2 for i in x) / len(x)

my_mean = data_mean(x1)
my_var = data_variance(x1)

numpy_mean = np.mean(x1)
numpy_var = np.var(x1)

np.testing.assert_approx_equal(my_mean, numpy_mean)
np.testing.assert_approx_equal(my_var, numpy_var)

def main():
   mean_x1 = data_mean(x1)
   mean_x2 = data_mean(x2)
   print(mean_x1)
   print(mean_x2)
   mean_diff = mean_x2 - mean_x1
   print(data_variance(x1))
   print(data_variance(x2))
   print(data_variance(x))
main()

# Q: Can you explain why the difference takes this value?
# A: Because we simply added 5 of each element in the array to x2 so the mean would increase by 5

# What is the relationship between the sample means of 'x1', 'x2', and 'x'?
# A: x2 - 5 = x1, x2 - 2.5 = x