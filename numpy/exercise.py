# NumPy Exercise
# 1)
import numpy as np

# 2)
print(str(np.zeros(10)) + '\n')

# 3)
print(str(np.ones(10)) + '\n')

# 4)
fives = np.ones(10)
fives[:] = 5
print(str(fives) + '\n')

# 5)
print(str(np.arange(10, 51)) + '\n')

# 6)
print(str(np.arange(10, 51, 2)) + '\n')

# 7)
print(str(np.arange(0, 9).reshape(3, 3)) + '\n')

# 8)
print(str(np.eye(3)) + '\n')

# 9)
print(np.random.rand(1))
