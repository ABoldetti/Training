import numpy as np
import matplotlib.pyplot as plt

# Define the function for the Taylor series
def taylor_series(x, n):
    result = 0
    for i in range(1,n):
        result += (np.power(x,i))/i
    return result

# Define the range of x values
x = np.linspace(-1, 1)

# Define the number of terms in the Taylor series
n = 100

# Calculate the y values using the Taylor series
y = taylor_series(x, n)

# Plot the Taylor series
plt.plot(x, y, label=f'Taylor series (n={n})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Taylor Series')
plt.legend()
plt.grid(True)
plt.show()