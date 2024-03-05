import os
import pandas as pd
import matplotlib.pyplot as plt

# # Sample data (replace this with your actual data)
# excel_file_path = os.path.join('data', 'data.xlsx')
# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file_path)

# # Create DataFrame
# df = pd.DataFrame(data)

# Define the file path
file_path = 'data/data.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Filter data for 'Open' status
open_issues = df[df['Status'] == 'Open']

# Group by priority and count the number of issues
grouped_issues = open_issues.groupby('Priority').size()

# Plot the chart
plt.bar(grouped_issues.index, grouped_issues.values)

# Set labels and title
plt.xlabel('Priority')
plt.ylabel('Number of Issues')
plt.title('Number of Open Issues by Priority')

# Customize x-axis ticks
plt.xticks([1, 2, 3, 4])

# Customize y-axis ticks to display only whole numbers
plt.yticks(range(int(max(grouped_issues.values)) + 1))

# Show the plot
plt.show()
