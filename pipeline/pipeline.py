import sys
import pandas as pd

print(sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({'days': [1, 2], 'number_passengers': [100, 200]})
df['month'] = month
print(df.head())

df.to_parquet(f'output_{month}.parquet', index=False)