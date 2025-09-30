import pandas as pd

products = ['apples', 'oranges', 'Grapes', 'pineapples']

sales = {150, 200, 100, 90, 60}

sales_series = pd.Series(sales, index=products)

print(sales_series)

#print(sales_series)
print(sales_series['Grapes'])

total_sales = sales_series.sum()
print(total_sales)


#Reading and Writing Data


#Read data from a CSV File
df = pd.read_csv('your_dataset.csv')

#Write data to CSV File
df.to_csv('output_dataset.csv', index=False)
