import pandas as pd
import matplotlib.pyplot as plt


file_path = 'plastic-share.csv'
df = pd.read_csv(file_path)


print(df.head())

print(df.describe(include='all'))

print(df.info())

print("Column Names:")
print(df.columns)


plt.figure(figsize=(12, 8))

columns_to_compare = [
    'Share of waste recycled from total regional waste',
    'Share of waste incinerated from total regional waste',
    'Share of littered and mismanaged from total regional waste',
    'Share of waste landfilled from total regional waste'
]


for col in columns_to_compare:
    plt.plot(df['Year'], df[col], marker='o', label=col)


plt.title('Comparison of Waste Management Shares Over Years')
plt.xlabel('Year')
plt.ylabel('Share (%)')
plt.xticks(df['Year'], rotation=90)  
plt.legend()
plt.grid(True)
plt.tight_layout()


plt.show()



