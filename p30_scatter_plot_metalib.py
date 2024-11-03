import pandas as pd
import matplotlib.pyplot as plt

# Create a simple dictionary with 5 keys and lists of 10 values each
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 
             'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack'],
    'Age': [24, 30, 22, 35, 28, 26, 32, 21, 27, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 
             'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 
             'Dallas', 'San Jose']
}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Create a scatter plot of Age against Name
plt.figure(figsize=(10, 6))
plt.scatter(df['Name'], df['Age'], color='blue', marker='o')

# Adding title and labels
plt.title('Scatter Plot of Age by Name')
plt.xlabel('Name')
plt.ylabel('Age')

# Show grid
plt.grid()

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels for better visibility
plt.tight_layout()  # Adjust layout
plt.show()

