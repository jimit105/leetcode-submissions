# Approach 1: Filtering Data with Exclusion Criteria

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers[~customers['id'].isin(orders['customerId'])]

    df = df[['name']].rename(columns={'name': 'Customers'})

    return df
