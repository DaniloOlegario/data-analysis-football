import pandas as pd
from pandasql import sqldf

# Carrega o arquivo CSV em um DataFrame do pandas
df = pd.read_csv('football_matches_2024_2025.csv')

#Listando os jogos do manchester city fc
query_jogos_city = """
SELECT date_utc, home_team, away_team, fulltime_home, fulltime_away
FROM df
WHERE home_team = 'Manchester City FC' OR away_team = 'Manchester City FC';
"""

# Executa a consulta
resultado_jogos = sqldf(query_jogos_city)

# Imprime o resultado
print(resultado_jogos)