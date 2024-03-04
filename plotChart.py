import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the path to "My Documents" folder
my_documents_path = os.path.expanduser("~/Documents")  # This works for most Unix-based systems including macOS and Linux

# Construct the full path to the Excel file
excel_file_path = os.path.join(my_documents_path, 'data.xlsx')

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Assuming the columns are named 'Column1' and 'Column2', you can plot them
plt.figure(figsize=(10, 6))  # Set the size of the figure

# Plot the data
plt.plot(df['Column1'], df['Column3'], marker='o', linestyle='-')

# Set the title and labels
plt.title('Data from Excel Sheet')
plt.xlabel('Column1')
plt.ylabel('Column2')

# Show the plot
plt.grid(True)  # Add grid
plt.show()
plt.savefig('plot.png')