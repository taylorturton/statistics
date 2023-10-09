import numpy as np
import scipy.stats as stats

# Sample data (replace with your own data)
sample_data = np.array([35000, 32000, 38000, 34000, 36000])

# Calculate sample mean and standard error
sample_mean = np.mean(sample_data)
standard_error = stats.sem(sample_data)

# Set the desired confidence level (e.g., 95%)
confidence_level = 0.95

# Calculate the confidence interval
margin_of_error = stats.t.ppf((1 + confidence_level) / 2, df=len(sample_data) - 1) * standard_error
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)

# Print the results
print("Sample Mean:", sample_mean)
print("Confidence Interval:", confidence_interval)
