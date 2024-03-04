import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the path to "My Documents" folder
my_documents_path = os.path.expanduser("~/Documents")  # This works for most Unix-based systems including macOS and Linux

# Construct the full path to the Excel file
excel_file_path = os.path.join(my_documents_path, 'data.xlsx')

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Group categories with similar values
grouped_df = df.groupby('Value')['Category'].apply(list).reset_index()

# Sum the values within each group
grouped_df['Value'] = grouped_df['Value'] * grouped_df['Category'].apply(len)

# Plotting the pie chart
plt.figure(figsize=(8, 8))  # Set the size of the figure

# Extracting data from DataFrame
labels = grouped_df['Category']
sizes = grouped_df['Value']

# Plotting the pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

# Set the title
plt.title('Pie Chart of Categories')

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Show the plot
plt.show()
plt.savefig('plot.png')