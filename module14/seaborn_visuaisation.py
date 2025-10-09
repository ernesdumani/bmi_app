import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv')

print(df.info())

plt.figure(figsize=(18,6))
sns.histplot(df['Average IQ'])
plt.title('Histogram of Average IQ')
plt.xlabel('Average IQ')
plt.ylabel('Frequency')
plt.show()
