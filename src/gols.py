import pandas as pd
from pandasql import sqldf

# Carrega o arquivo CSV em um DataFrame do pandas
df = pd.read_csv('football_matches_2024_2025.csv')

# Calcule o total de gols por competição
query_gols_comp = """
SELECT competition_name, SUM(total_goals) AS total_gols
FROM df
GROUP BY competition_name;
"""

# Executa a consulta
resultado_gols = sqldf(query_gols_comp)

# Imprime o resultado
print(resultado_gols)