import pandas as pd
import matplotlib.pyplot as plt


file_path = 'Cleanest_Cities_India.csv'
df = pd.read_csv(file_path)


print(df.head())

print(df.describe(include='all'))

print(df.info())

print("Column Names:")
print(df.columns)


years = ['2023', '2022', '2020', '2019', '2018', '2017']
for year in years:
    df[year] = pd.to_numeric(df[year], errors='coerce')


def plot_pie_chart(year_data, year):
    
    year_data_sorted = year_data.sort_values(by=year, ascending=False)

  
    top_5 = year_data_sorted.head(5)
    
    zero_value_cities = year_data_sorted[year_data_sorted[year] == 0].head(15)

    top_5 = top_5.dropna(subset=[year])
    
    print(f"\nYear: {year}")
    print("Top 5 cities:")
    print(top_5)
    print("Cities with 0 values:")
    print(zero_value_cities['City Name'].tolist())

   
    fig, ax = plt.subplots(1, 2, figsize=(18, 9))

   
    if not top_5.empty:
        ax[0].pie(top_5[year], labels=top_5['City Name'], autopct='%1.1f%%', startangle=140)
        ax[0].set_title(f'Score of Top  Cities  - {year}')
    
    
    if not zero_value_cities.empty:
        zero_value_cities_list = zero_value_cities['City Name'].tolist()
        textstr = '\n'.join(zero_value_cities_list)
        ax[1].text(0.5, 0.5, textstr, horizontalalignment='center', verticalalignment='center', transform=ax[1].transAxes, fontsize=12)
        ax[1].set_title(f'Cities with low score - {year}')
        ax[1].axis('off')

    plt.tight_layout()
    plt.show()


for year in years:
    plot_pie_chart(df[['City Name', year]], year)