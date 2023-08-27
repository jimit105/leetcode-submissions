import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
  df = products.melt(id_vars='product_id', var_name='store', value_name='price')
  df = df.dropna(axis=0)
  return df
