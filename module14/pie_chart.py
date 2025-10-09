import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("avgIQpercountry.csv")

nobel_prizes_per_country = df.groupby('Continent')['Nobel Prices'].sum()


no_af_continents = nobel_prizes_per_country.count()

print(no_af_continents)

colors = {'gold', 'lightcoral', 'yellow', 'red', 'orange', 'blue', 'aquamarine', 'brown'}

plt.figure(figsize = (10,10))

nobel_prizes_per_country.plot(kind='pie', colors=colors, autopct = '1%1.1f%%')

plt.title('Distribution of Nobel Prizes by Continent')

plt.axis('equal')

plt.ylabel('')

plt.tight_layout()

plt.show()