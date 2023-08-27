import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
  df = employee[['salary']].drop_duplicates()
  if len(df) < N:
    return pd.DataFrame({f'getNthHighestSalary({N})' : [None]})
  return df.sort_values('salary', ascending=False).head(N).tail(1)[['salary']]
