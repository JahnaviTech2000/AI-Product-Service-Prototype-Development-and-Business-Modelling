import pandas as pd
import matplotlib.pyplot as plt


file_path = 'plastic-production.csv'
df = pd.read_csv(file_path)


print(df.head())

print(df.describe(include='all'))

print(df.info())

print("Column Names:")
print(df.columns)



df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
df['Annual plastic production'] = pd.to_numeric(df['Annual plastic production '], errors='coerce') 


df = df.sort_values(by='Year')


plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['Annual plastic production'], marker='o', linestyle='-')
plt.title('Annual Plastic Production Over Years')
plt.xlabel('Year')
plt.ylabel('Annual Plastic Production')
plt.grid(True)
plt.tight_layout()
plt.show()
