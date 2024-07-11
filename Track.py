import pandas as pd

# Sample data (you can replace this with your actual data)
data = {
    "Project Name": ["Project A", "Project B", "Project C"],
    "Milestone": ["M1", "M2", "M3"],
    "Completion Date": ["2023-01-10", "2023-01-15", "2023-01-20"],
    "Planned Date": ["2023-01-10", "2023-01-14", "2023-01-18"],
    "Status": ["Completed", "Completed", "Not Completed"]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# Convert date columns to datetime format
df["Completion Date"] = pd.to_datetime(df["Completion Date"])
df["Planned Date"] = pd.to_datetime(df["Planned Date"])

# Add a new column "On Track" based on the criteria
df["On Track"] = (df["Status"] == "Completed") & (df["Completion Date"] <= df["Planned Date"])

# Print the updated DataFrame
print(df)