# Задача 40:
import pandas as pd
data = pd.read_csv('california_housing_test.csv')
print(data[ data['population'] < 500 ]['median_house_value'].mean())

# Задача 42:
print(data[data['population'] == data['population'].min()]['households'].max())