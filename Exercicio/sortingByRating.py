import pandas as pd
import re

# Suponha que as colunas sejam: Título, Ano, Nota, Sinopse
colunas = ["Titulo", "Ano", "Nota", "Sinopse"]
df = pd.read_csv("movies.csv", header=None, names=colunas)

print(df.head())

def extrai_nota(rating_str):
    match = re.search(r"(\d+\.?\d*)", str(rating_str))
    if match:
        return float(match.group(1))
    return None

df["Rating_Num"] = df["Nota"].apply(extrai_nota)
df_sorted = df.sort_values(by="Rating_Num", ascending=False)

print(df_sorted)

df_sorted.to_csv("sorted_movies.csv", index=False)
