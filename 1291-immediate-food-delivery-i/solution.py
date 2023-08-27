import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
  is_valid = delivery['order_date'] == delivery['customer_pref_delivery_date']
  
  valid_count = is_valid.sum()
  total = len(delivery)

  percent = round(100 * valid_count / total, 2)

  return pd.DataFrame({'immediate_percentage': [percent]})
