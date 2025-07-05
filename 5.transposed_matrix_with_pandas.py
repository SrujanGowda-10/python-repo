# With pandas
import pandas as pd

a = [[3, 4, 5],
     [7, 8, 9],
     [2, 1, 0]]

# Convert to DataFrame
df = pd.DataFrame(a)

# Transpose the DataFrame
transposed_df = df.T

# Convert back to list of lists (optional)
transposed_list = transposed_df.values.tolist()

print(transposed_df)
print(transposed_list)
