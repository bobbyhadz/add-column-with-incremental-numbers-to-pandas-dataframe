# Add a column with incremental Numbers to a Pandas DataFrame

import pandas as pd

df = pd.DataFrame({
    'name': ['Alice', 'Bobby', None, None],
    'experience': [None, 5, None, None],
    'salary': [None, 180.2, 190.3, 205.4],
})

#     name  experience  salary
# 0  Alice         NaN     NaN
# 1  Bobby         5.0   180.2
# 2   None         NaN   190.3
# 3   None         NaN   205.4
print(df)

df.insert(0, 'ID', range(0, 0 + len(df)))

#    ID   name  experience  salary
# 0   0  Alice         NaN     NaN
# 1   1  Bobby         5.0   180.2
# 2   2   None         NaN   190.3
# 3   3   None         NaN   205.4
print(df)