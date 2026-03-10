import pandas as pd

# Carrega dataframes - Ignorando título da planilha e separado pelo nome da aba
org_traffic  = pd.read_excel("data/dados_player1.xlsx", sheet_name="Organic traffic", skiprows=1)
org_cost     = pd.read_excel("data/dados_player1.xlsx", sheet_name="Organic cost", skiprows=1)
ad_traffic   = pd.read_excel("data/dados_player1.xlsx", sheet_name="Adwords traffic", skiprows=1)
org_keywords = pd.read_excel("data/dados_player1.xlsx", sheet_name="Organic keywords", skiprows=1)

# Salva os dados dos dataframes separadamente em arquivos .csv
org_traffic.to_csv("data/csv/org_traffic.csv", index=False)
org_cost.to_csv("data/csv/org_cost.csv", index=False)
ad_traffic.to_csv("data/csv/ad_traffic.csv", index=False)
org_keywords.to_csv("data/csv/org_keywords.csv", index=False)