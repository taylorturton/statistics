import scipy.stats as stats

# Sample data for the original and new training programs
data_original = [10.00, 12.00, 11.00, 12.50, 13.50]
data_new = [9.50, 12.00, 10.50, 13.00, 13.00]

# Perform a two-sample t-test
t_statistic, p_value = stats.ttest_ind(data_original, data_new)

# Print the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)
