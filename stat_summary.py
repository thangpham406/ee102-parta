import pandas as pd

# Load the data
file_path = '~/Desktop/Thang/Data_Split.xlsx'

file =pd.read_excel(file_path)
training_data = pd.read_excel(file_path, sheet_name='Training Data')
test_data = pd.read_excel(file_path, sheet_name='Test Data')

file.info()



''' 
Calculate the summary statistics for the training and test data
find mean, median, mode, minimum, maximum, variance, and standard deviation
for each column in the training and test data.
'''
def stat_summary(data):
    stat = pd.DataFrame({
        'Mean': data.mean(),
        'Median': data.median(),
        'Mode': data.mode().iloc[0],
        'Minimum': data.min(),
        'Maximum': data.max(),
        'Variance': data.var(),
        'Standard Deviation': data.std()
    })
    return stat

print("Training Data Summary:\n")
print(stat_summary(training_data))

print("\nTest Data Summary:\n")
print(stat_summary(test_data))

import matplotlib.pyplot as plt
# Create a scatter plot matrix for all columns
scatter_matrix = pd.plotting.scatter_matrix(training_data, alpha=0.2, figsize=(12, 12), diagonal='kde')

# Adjust the rotation of x and y labels for better readability
for ax in scatter_matrix.ravel():
    ax.set_xlabel(ax.get_xlabel())
    ax.set_ylabel(ax.get_ylabel())

# Tight layout to ensure labels don't overlap
plt.tight_layout()

# Show the plot
plt.show()
plt.close()


# Calculate the correlation coefficients between the input variables and the output PE column
#Correlation Coefficient for input and output
def cor_coe(var ):
    input_var = training_data[var]
    output_var = training_data['PE']
    correlation = input_var.corr(output_var)
    
    return correlation
print("Correlation Coefficient for input and output:\n")
#format the output for better readability and 3 decimal places
print('AT:', format(cor_coe('AT'), '.3f'))
print('V:', format(cor_coe('V'), '.3f'))
print('AP:', format(cor_coe('AP'), '.3f'))

