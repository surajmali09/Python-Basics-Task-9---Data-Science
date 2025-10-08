import pandas as pd


data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'David'],
    'Age': [25, 30, 25, 35],
    'City': ['New York', 'Los Angeles', 'New York', 'Chicago']
})


data.drop_duplicates(inplace=True)


data.columns = [col.strip().lower() for col in data.columns]


data = data[['name', 'city', 'age']]

print(data)
