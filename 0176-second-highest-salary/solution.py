import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
  employee = employee.drop_duplicates(['salary'])
  if len(employee['salary'].unique()) < 2:
    return pd.DataFrame({"SecondHighestSalary" : [None]})

  employee = employee.sort_values('salary', ascending=False)
  employee.drop('id', axis=1, inplace=True)
  employee.rename({'salary': 'SecondHighestSalary'}, axis=1, inplace=True)
  return employee.head(2).tail(1)
