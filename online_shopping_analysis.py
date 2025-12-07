from sqlalchemy import create_engine
import pandas as pd 

df = pd.read_csv('online_shopping_dataset.csv')
print(df.describe())
# print(df.info())
# df.to_csv('online_shopping_dataset.csv', index=False)
# print(df)

# print(df.isnull().sum())
# df['review_rating'] = df.groupby('category')['review_rating'].transform(lambda x: x.fillna(x.median()))
# df.to_csv('online_shopping_dataset.csv', index=False)

# df.columns = df.columns.str.lower()
# df.columns = df.columns.str.replace(' ','_')
# df.to_csv('online_shopping_dataset.csv', index=False)


# df = df.rename(columns={'purchase_amount_(usd)' : 'purchase_amount'})
# df.to_csv('online_shopping_dataset.csv', index=False)


# labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
# df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)
# df.to_csv('online_shopping_dataset.csv', index=False)

# frequency_mapping = {
#     'Fortnightly': 14,
#     'Weekly': 7,
#     'Monthly': 30,
#     'Quarterly': 90,
#     'Bi-Weekly': 14,
#     'Annually': 365,
#     'Every 3 Months': 90
# }

# df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
# df.to_csv('online_shopping_dataset.csv', index=False)


# df = df.drop('promo_code_used', axis=1)

# df.to_csv('online_shopping_dataset.csv', index=False)


# username = "postgres"      
# password = "postgres" 
# host = "localhost"         
# port = "5432"             
# database = "postgres"    

# engine = create_engine(f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}")

# table_name = "customer"   
# df.to_sql(table_name, engine, if_exists="replace", index=False)

# print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")
