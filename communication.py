#communication control will run here gsm
import numpy as np

# Sample list of names
names = np.array(["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivy", "Jack"])

# Sample list of indexes as a NumPy array
indexes = np.array([])

if indexes.size == 0:
    print("The 'indexes' array is empty.")
else:
    # Find the names corresponding to the indexes
    selected_names = names[indexes]
    
    # Print the selected names
    for name in selected_names:
        print(name)
