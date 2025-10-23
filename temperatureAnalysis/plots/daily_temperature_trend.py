import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = r"../data/temperatures.csv"  # Adjust path relative to this script
df = pd.read_csv(data_path)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Debug: Inspect data
print("First 10 rows of year and day:")
print(df[['year', 'day']].head(10))

# Clean data: Ensure year is valid
df = df[df['year'].notna() & df['day'].notna()]
df = df[df['year'].astype(str).str.match(r'^\d{4}$')]  # 4-digit years

# Convert 'day' from MM/DD to proper date format
# Combine year and day into 'YYYY-MM-DD'
df['date_str'] = df['year'].astype(str) + '-' + df['day'].str.replace('/', '-')  # Convert 11/6 to 11-06
print("Combined date strings:")
print(df['date_str'].head(10))

# Parse into datetime
df['date'] = pd.to_datetime(df['date_str'], format='%Y-%m-%d', errors='coerce')

# Check for invalid dates
if df['date'].isna().any():
    print("Invalid dates found:")
    print(df[df['date'].isna()][['year', 'day', 'date_str']])
    df = df.dropna(subset=['date'])  # Drop invalid dates

# Daily temperature trend plot
plt.figure(figsize=(12, 4))
plt.plot(df['date'], df['temperature'], color='blue')
plt.title('Daily Temperature Trend - Tokyo')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()

# Make sure the plots directory exists
os.makedirs('plots', exist_ok=True)
plt.savefig('plots/daily_temperature_trend.png')
plt.close()

print("✅ Daily temperature trend plot saved as 'plots/daily_temperature_trend.png'")