import pandas as pd

path = input("Enter the file path of your dataset without double quotes: ")
data = pd.read_csv(path)
cleaned = data.drop_duplicates()

print(f"Original number of rows: {data.shape[0]}\n")
print(f"Number of rows after removing duplicates: {cleaned.shape[0]}\n")

output = input("Enter the output file path for the cleaned dataset without double quotes: ")
cleaned.to_csv(output, index=False)

print("Duplicates removed and cleaned data saved.")
