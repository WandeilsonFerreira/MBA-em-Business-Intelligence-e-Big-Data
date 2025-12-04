import pandas as pd

def csv_para_xlsx(arquivo_csv, arquivo_xlsx):
    # Lê o arquivo CSV
    df = pd.read_csv(arquivo_csv)

    # Salva como arquivo XLSX
    df.to_excel(arquivo_xlsx, index=False)

    print(f"Arquivo {arquivo_csv} convertido para {arquivo_xlsx} com sucesso!")

# Exemplo de uso
csv_para_xlsx("produtos.csv", "produtos.xlsx")