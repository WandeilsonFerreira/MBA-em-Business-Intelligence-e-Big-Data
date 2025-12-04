import pandas as pd

#Carregando todos os arquivos do modelo
arquivos_csv = ['base/202001.csv', 'base/202002.csv', 'base/202101.csv', 'base/202101.csv','base/202201.csv', 'base/202202.csv', 'base/202301.csv','base/202302.csv','base/202401.csv','base/202402.csv','base/202501.csv','base/202502.csv','base/202503.csv','base/202504.csv','base/202506.csv',]

lista_df = []

for i, arquivo in enumerate(arquivos_csv):
    if i == 0:
        # Lê com cabeçalho na primeira iteração
        temp_df = pd.read_csv(arquivo, sep=';')
    else:
        # Lê sem cabeçalho nas próximas
        temp_df = pd.read_csv(arquivo, sep=';', header=None)
        temp_df.columns = lista_df[0].columns  # Atribui colunas da primeira base
    lista_df.append(temp_df)

df_final = pd.concat(lista_df, ignore_index=True)

# Salva o DataFrame como CSV
df_final.to_csv('base/Valor_combustivel_Brasil_2020_2025.csv', sep=';', index=False, encoding='utf-8')

