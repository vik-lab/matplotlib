import os
import pandas as pd
import matplotlib.pyplot as plt

excel_file_path = os.path.join('data', 'data.xlsx')
# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Group categories with similar values and sum the values within each group
grouped_df = df.groupby('Issue.No')['Priority'].sum().reset_index()

# Extracting data from DataFrame
labels = grouped_df['Issue.No']
sizes = grouped_df['Priority']

# Plotting the pie chart
plt.figure(figsize=(8, 8))  # Set the size of the figure
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Categories')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()
