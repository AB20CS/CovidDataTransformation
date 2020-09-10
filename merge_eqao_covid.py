import pandas as pd

df_eqao = pd.read_csv('eqao_aggregated_data.csv')
df_covid = pd.read_csv('covid_transformed.csv')
df_merged = df_eqao.merge(df_covid, on='PHU')

df_merged.to_csv("covid_merged_data.csv", index=False)
