# ⚽ Análise Exploratória de Dados Esportivos (Python/Pandas/SQL)

## 🎯 Objetivo de Negócio

Este projeto visa extrair *insights* valiosos de um conjunto de dados de partidas de futebol (`football_matches_2024_2025.csv`) para responder a perguntas estratégicas sobre performance de times e competições.

**Foco:** Demonstrar proficiência em **manipulação de dados (Pandas)** e **consultas estruturadas (SQL)** em um ambiente Python.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Pandas:** Manipulação, limpeza e agregação de dados.
* **PandasQL:** Habilidade de realizar consultas SQL complexas diretamente em DataFrames.
* **[Nome da Biblioteca de Visualização que você usaria, ex: Matplotlib/Seaborn]** (Para visualização)

---

## 🔍 Perguntas Chave Respondidas (Insights)

A análise foi conduzida usando o conjunto de dados para responder a perguntas típicas do negócio esportivo:

1.  **Time Mais Vencedor:** Qual time demonstrou maior domínio, contabilizando o maior número total de vitórias (em casa e fora) na temporada?
    * **Insight:** **[Mencione o time que você encontrou]** demonstrou a maior consistência, registrando **[X]** vitórias no total.
2.  **Performance por Competição:** Como o volume de gols se distribui entre as diferentes competições (Ex: Premier League, Champions League)?
    * **Insight:** A **[Nome da Competição]** registrou o maior volume de gols, indicando [Sua interpretação sobre o placar ou nível de ataque].
3.  **Filtro Específico:** Qual foi o histórico de jogos e resultados do time **Manchester City FC** na temporada?
    * **Insight:** O time demonstrou uma forte performance em **[Seu Insight: Ex: jogos em casa]**, mas teve dificuldades em **[Seu Insight: Ex: jogos fora de casa]**.

---

## ⚙️ Estrutura do Projeto

* `data/`: Contém a fonte de dados (`football_matches_2024_2025.csv`).
* `src/main.py`: Script Python principal que demonstra a lógica de agregação e filtragem usando **PandasQL**.
* `src/gols.py`: Script de suporte para análise de volume total de gols por competição.
* `notebooks/`: Onde a análise mais detalhada e as visualizações (gráficos) seriam realizadas (em desenvolvimento).

## 🚀 Como Executar

1.  Clone o repositório.
2.  Instale as dependências: `pip install pandas pandasql`
3.  Execute o script principal para ver os resultados no terminal: `python src/main.py`

---

Após criar este `README.md`, você pode seguir com o **upload dos arquivos** para um novo repositório no GitHub. Quer ajuda com os comandos Git?