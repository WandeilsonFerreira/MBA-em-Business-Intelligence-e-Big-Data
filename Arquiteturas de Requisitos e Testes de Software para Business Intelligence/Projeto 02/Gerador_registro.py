import pandas as pd
# import numpy as np
import random

#Ler o arquivo original 
arquivo_original = 'Arquivo_licit_final_categorizado.xlsx'  # Substitua pelo caminho do arquivo original
tabela_original = pd.read_excel(arquivo_original)

# Lista de cidades da Paraíba
cidades_paraiba = [
    "João Pessoa", "Campina Grande", "Santa Rita", "Patos", "Bayeux",
    "Sousa", "Cabedelo", "Cajazeiras", "Guarabira", "Sapé",
    "Mamanguape", "Queimadas", "Monteiro", "Esperança", "Pombal",
    "Itabaiana", "Catolé do Rocha", "Alagoa Grande", "Conde", "Solânea",
    "Pedras de Fogo", "Areia", "Bananeiras", "Itaporanga", "Piancó"
]


funcionalidades = [
    "Aquisição de materiais diversos (elétricos, construção, esportivos, etc.)",
    "Fornecimento de alimentos e produtos para merenda escolar e eventos",
    "Contratação de serviços especializados (manutenção, locação de veículos, engenharia)",
    "Realização de eventos culturais e artísticos",
    "Aquisição de itens tecnológicos (equipamentos de informática, software)",
    "Obras de infraestrutura (reformas, pavimentação, construção)",
    "Assistência social (cestas básicas, serviços funerários, etc.)",
    "Contratação de serviços para mobilidade e transporte",
    "Prestação de serviços administrativos (consultorias, assessorias jurídicas)",
    "Locação de imóveis para funcionamento de órgãos municipais e sociais",
    "Organização de atividades pedagógicas e treinamentos para servidores públicos",
    "Planejamento e execução de festividades tradicionais, incluindo shows artísticos",
    "Aquisição de combustíveis e produtos para manutenção de frota municipal",
    "Execução de projetos cenográficos e arquitetônicos para eventos culturais",
    "Contratação de serviços gráficos e produção de materiais pedagógicos",
    "Locação de equipamentos para suporte técnico e operacional em eventos",
    "Aquisição de materiais de limpeza, higiene e outros insumos para órgãos públicos",
    "Prestação de serviços de segurança, ornamentação e apoio em festividades",
    "Locação de espaços para armazenamento e guarda de bens públicos",
    "Fornecimento de serviços de transmissão digital para eventos culturais",
]


# Criar novos registros fictícios
novos_registros = []
for i in range(10000):
    registro_ficticio = {
        "Modalidade": random.choice(["PREGÃO ELETRÔNICO", "CONCORRÊNCIA ELETRÔNICA", "DISPENSA POR VALOR"]),
        "Objeto": random.choice(funcionalidades),
        "Data": "2025-12-31",
        "Cod. Órgão": 201000 + i,
        "Órgão": f"PREFEITURA MUNICIPAL DE {random.choice(cidades_paraiba).upper()}",
        "Valor Estimado": round(random.uniform(10000, 1000000), 2),
        "Valor": round(random.uniform(5000, 900000), 2),
        "Homologação": random.choice(["EM ANDAMENTO", "FINALIZADA"]),
        "Situação": "COMPRA E SERVIÇOS",
        "Tipo Objeto": random.choice(["Saúde e Medicamentos", "Obras e Engenharia", "Outros", "Veículos e Transporte"]),
        "Categoria": random.choice(["Saúde", "Infraestrutura", "Assistência Social", "Tecnologia", "Alimentos"])
    }
    novos_registros.append(registro_ficticio)

# Converter os novos registros em um DataFrame e adicionar à tabela original
novos_dados = pd.DataFrame(novos_registros)
tabela_completa = pd.concat([tabela_original, novos_dados], ignore_index=True)

# Salvar o novo arquivo Excel
novo_arquivo = "Arquivo_licit_final_categorizado_com_ficticios.xlsx"
tabela_completa.to_excel(novo_arquivo, index=False)

print(f"Arquivo atualizado salvo como: {novo_arquivo}")
