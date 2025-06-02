import pandas as pd

# Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Preview data
print("Initial data shape:", df.shape)
print(df.info())

# Drop duplicates
df.drop_duplicates(inplace=True)

# Handle missing values
df.fillna({'director': 'Unknown', 'cast': 'Unknown', 'country': 'Unknown'}, inplace=True)

# Fix date format
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Clean column names
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

# Fix inconsistent text values
df['type'] = df['type'].str.title()
df['rating'] = df['rating'].str.upper()

# Export cleaned data
df.to_csv('cleaned_netflix_data.csv', index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'cleaned_netflix_data.csv'")
