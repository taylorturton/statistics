import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# Data for time spent in the gym and duels won
time_in_gym = np.array([50, 28, 17, 39, 65])
duels_won = np.array([26, 14, 8, 40, 52])

# Perform linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(time_in_gym, duels_won)

# Create a scatter plot of the data points
plt.scatter(time_in_gym, duels_won, label='Data Points')

# Create a line for the regression equation
regression_line = slope * time_in_gym + intercept

# Add the regression line to the plot
plt.plot(time_in_gym, regression_line, color='red', label='Regression Line')

# Set labels and title
plt.xlabel('Time Spent in Gym (hours)')
plt.ylabel('Duels Won')
plt.title('Time in Gym vs. Duels Won')

# Display the equation of the regression line on the plot
equation = f'Y = {slope:.2f}X + {intercept:.2f}\nR-squared = {r_value**2:.2f}'
plt.text(30, 45, equation, fontsize=12, color='blue')

# Add a legend
plt.legend()

# Show the plot
plt.show()
