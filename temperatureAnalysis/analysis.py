import pandas as pd
import matplotlib.pyplot as plt
import os

# Load dataset
data_path = r"data/temperatures.csv"
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
df['temperature'] = df['temperature'].str.split().str[0]  # Take first value
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

# 1. Overall Average Temperature
overall_avg = round(df['temperature'].mean(), 2)
print(f"🌡️ Overall Average Temperature: {overall_avg} °C")

# 2. Hottest and Coldest Days
hottest = df.loc[df['temperature'].idxmax()]
coldest = df.loc[df['temperature'].idxmin()]
print(f"🔥 Hottest Day: {hottest['date'].date()} with {hottest['temperature']} °C")
print(f"❄️ Coldest Day: {coldest['date'].date()} with {coldest['temperature']} °C")

# 3. Daily Temperature Trend
plt.figure(figsize=(12, 4))
plt.plot(df['date'], df['temperature'], color='blue')
plt.title('Daily Temperature Trend - Tokyo')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
os.makedirs('plots', exist_ok=True)  # Ensure plots directory exists
plt.savefig('plots/daily_temperature_trend.png')
plt.close()

# 4. Monthly Average Temperature
df['month'] = df['date'].dt.to_period('M').dt.to_timestamp()
monthly_avg = df.groupby('month')['temperature'].mean().round(2).reset_index()

plt.figure(figsize=(10, 4))
plt.bar(monthly_avg['month'].dt.strftime('%Y-%m'), monthly_avg['temperature'], color='orange')
plt.title('Monthly Average Temperature - Tokyo')
plt.xlabel('Month')
plt.ylabel('Avg Temperature (°C)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('plots/monthly_average_bar.png')
plt.close()

# 5. Seasonal Average Temperature
def month_to_season(month):
    if month in (12, 1, 2):
        return 'Winter'
    if month in (3, 4, 5):
        return 'Spring'
    if month in (6, 7, 8):
        return 'Summer'
    return 'Autumn'

df['season'] = df['date'].dt.month.apply(month_to_season)
seasonal_avg = df.groupby('season')['temperature'].mean().reindex(['Winter', 'Spring', 'Summer', 'Autumn']).round(2).reset_index()

plt.figure(figsize=(6, 4))
plt.bar(seasonal_avg['season'], seasonal_avg['temperature'], color='green')
plt.title('Seasonal Average Temperature - Tokyo')
plt.xlabel('Season')
plt.ylabel('Avg Temperature (°C)')
plt.tight_layout()
plt.savefig('plots/seasonal_average.png')
plt.close()

print("✅ All plots saved in 'plots/' folder")