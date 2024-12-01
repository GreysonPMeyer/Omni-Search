import pandas as pd
df = pd.read_csv('/Users/greysonmeyer/Desktop/Erdos_Work/omni_data_cleaned_to_be_split.csv')

# Calculate the size of each smaller file
split_size = len(df) // 3

# Split the DataFrame into three smaller DataFrames
df1 = df.iloc[:split_size]
df2 = df.iloc[split_size:split_size*2]
df3 = df.iloc[split_size*2:]

# Save each DataFrame to a new CSV file
df1.to_csv('split_file_1.csv', index=False)
df2.to_csv('split_file_2.csv', index=False)
df3.to_csv('split_file_3.csv', index=False)

print("CSV file successfully split into three smaller files.")