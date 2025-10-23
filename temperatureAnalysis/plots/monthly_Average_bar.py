import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = r"../data/temperatures.csv"  # Adjust path relative to this script
df = pd.read_csv(data_path)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Debug: Print column names and first few rows
print("Columns in DataFrame:", df.columns)
print("First 10 rows of year, day, and temperature:")
print(df[['year', 'day', 'temperature']].head(10))
print("Unique temperature values:")
print(df['temperature'].unique()[:10])

# Clean data: Ensure year and day are valid
df = df[df['year'].notna() & df['day'].notna()]
df = df[df['year'].astype(str).str.match(r'^\d{4}$')]  # 4-digit years

# Clean temperature: Handle space-separated values and convert to numeric
df['temperature'] = df['temperature'].str.split().str[0]  # Take first value if space-separated
# Alternative: If you need the mean of multiple values in a cell:
# df['temperature'] = df['temperature'].str.split().apply(lambda x: pd.Series(x).astype(float).mean() if isinstance(x, list) else x)
df['temperature'] = pd.to_numeric(df['temperature'], errors='coerce')

# Check for invalid temperatures
if df['temperature'].isna().any():
    print("Invalid temperature values found:")
    print(df[df['temperature'].isna()][['year', 'day', 'temperature']])
    df = df.dropna(subset=['temperature'])  # Drop invalid temperatures

# Convert 'day' from MM/DD to YYYY-MM-DD
df['date_str'] = df['year'].astype(str) + '-' + df['day'].str.replace('/', '-')  # Convert 11/6 to 11-06
df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d', errors='coerce')

# Check for invalid dates
if df['date'].isna().any():
    print("Invalid dates found:")
    print(df[df['date'].isna()][['year', 'day', 'date_str']])
    df = df.dropna(subset=['date'])  # Drop invalid dates

# Extract month name for grouping
df['month'] = df['date'].dt.strftime('%B')  # Full month name (e.g., January)

# Calculate monthly average temperatures
monthly_avg = df.groupby('month')['temperature'].mean().reindex([
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
])

# Monthly average temperature bar plot
plt.figure(figsize=(10, 6))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title('Monthly Average Temperature - Tokyo')
plt.xlabel('Month')
plt.ylabel('Average Temperature (°C)')
plt.tight_layout()

# Make sure the plots directory exists
os.makedirs('plots', exist_ok=True)
plt.savefig('plots/monthly_average_bar.png')
plt.close()

print("✅ Monthly average temperature bar plot saved as 'plots/monthly_average_bar.png'")