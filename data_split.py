import pandas as pd

# Load the data from the second sheet of the Excel file
file_path = '~/Desktop/Thang/Folds5x2_pp.xlsx'
data = pd.read_excel(file_path, sheet_name=1)  # Sheet names are zero-indexed

# Determine the number of rows for training (80% of the total data)
total_rows = len(data)
training_rows = int(0.8 * total_rows)

# Split the data into training and test sets
training_data = data.iloc[:training_rows]
test_data = data.iloc[training_rows:]

# Save the training and test data into separate sheets of a new Excel file
output_file = 'Data_Split.xlsx'
with pd.ExcelWriter(output_file) as writer:
    training_data.to_excel(writer, sheet_name='Training Data', index=False)
    test_data.to_excel(writer, sheet_name='Test Data', index=False)


