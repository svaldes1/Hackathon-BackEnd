# Iphone 15 Pro Max,Iphone 15 Pro, Iphone 15, Iphone 14 pro max, Iphone 14, Iphone 13
#  Samsung Galaxy S23 Ultra, Samsung Galaxy S23, Samsung Galaxy S22,Samsung Galaxy S21, Samsung Galaxy Z Flip5
# Motorola one 5G UW ace, Google Pixel 7a, Google Pixel Fold,Motorola edge - 2022, Google Pixel 7, Google Pixel 6a

# list = [["Iphone 15 Pro Max","Iphone 15 Pro"," Iphone 15"", Iphone 14 pro max"," Iphone 14"," Iphone 13"],
#         ["Samsung Galaxy S23 Ultra"," Samsung Galaxy S23"," Samsung Galaxy S22","Samsung Galaxy S21"," Samsung Galaxy Z Flip5"],
#         ["Motorola one 5G UW ace"," Google Pixel 7a"," Google Pixel Fold,Motorola edge - 2022"," Google Pixel 7"," Google Pixel 6a"]]

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skewnorm

# Define the parameters for the skew normal distribution
alpha = -1.5  # Adjust this parameter for different levels of skewness
loc = 7 # Mean
scale = 0.95   # Standard deviation
num_samples = 20000
down_bound = 0
up_bound = 10


def hist_show(samples):
      # Create a histogram of the generated samples
   plt.hist(samples, bins=30, density=True, alpha=0.6, color='b', label='Skewed Normal Distribution')

   # Plot the PDF of the skew normal distribution for reference
   x = np.linspace(samples.min(), samples.max(), 1000)
   pdf = skewnorm.pdf(x, alpha, loc=loc, scale=scale)
   plt.plot(x, pdf, 'r-', lw=2, label='PDF')

   # Add labels and a legend
   plt.xlabel('Value')
   plt.ylabel('Probability Density')
   plt.legend()

   plt.title('Skewed Normal Distribution')
   plt.show()


# Generate samples from the skew normal distribution
samples = skewnorm.rvs(alpha, loc=loc, scale=scale, size=num_samples)
samples = np.where(samples > up_bound, up_bound, samples)
samples = np.where(samples < down_bound, down_bound, samples)

hist_show(samples)

# Create dataframe

# def product_funct(apple, samsung, Google):

#    list = [["Iphone 15 Pro Max","Iphone 15 Pro"," Iphone 15"", Iphone 14 pro max"," Iphone 14"," Iphone 13"],
#          ["Samsung Galaxy S23 Ultra"," Samsung Galaxy S23"," Samsung Galaxy S22","Samsung Galaxy S21"," Samsung Galaxy Z Flip5"],
#          ["Google Pixel 7a","Google Pixel Fold"," Google Pixel 7"," Google Pixel 6a"],
#          ["Motorola one 5G UW ace", "Motorola edge - 2022"]]

#    # Random num between 0 and 1
#    rand_num = np.random.rand(1)

#    if rand_num < apple:
#       product = np.random.choice(list[0])

#    elif rand_num < apple + samsung:
#       product = np.random.choice(list[1])

#    elif rand_num < apple + samsung + Google:
#       product = np.random.choice(list[2])

#    else:
#       product = np.random.choice(list[3])
   
#    return product


# print(product_funct(0.8, 0.05, 0.05))