import pandas as pd
from pandasql import sqldf


# Carrega o arquivo CSV em um DataFrame do pandas.
# O nome do DataFrame será "df" para usá-lo nas queries SQL.
df = pd.read_csv('football_matches_2024_2025.csv')


#
query ="""
SELECT home_team, COUNT(*) AS total_vitorias
FROM df
WHERE match_outcome = 'Home Win'
GROUP BY home_team
ORDER BY COUNT(*) DESC
LIMIT 5;


SELECT date_utc, home_team, away_team, fulltime_home, fulltime_away
FROM df
WHERE home_team = 'Manchester City FC' OR away_team = 'Manchester City FC';

SELECT competition_name, SUM(total_goals) AS total_gols
FROM df
GROUP BY competition_name;
"""

# Executa a consulta e armazena o resultado em uma nova variável
vitorias_em_casa = sqldf(query)

# Imprime o resultado para visualização
print(vitorias_em_casa)