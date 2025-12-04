### MBA BI BIG DATA T8 
#### Machine Learning: Tópicos Avançados
##### Analise de combustiveis brasileiros 
##### Wandeilson Ferreira 
## Sobre o Projeto

Este projeto tem como objetivo a análise estatística dos valores de combustiveis no Brasil ao longo dos ultimos 5 anos, utilizando ETL para a transformação e armazenamento dos dados. Através da modelagem e processamento eficiente, buscamos identificar a discrepancia no valor do combustivel a nivel nacional. 


### Arquitetura do Projeto

###  ETL (Extract, Transform, Load)
- Extração de dados de arquivos brutos 
    - Para o experimento foi utilizada a base de dados publicas "dados abertos" disponibilizada pelo governo federal e disponivel atraves do [link](https://dados.gov.br/dados/conjuntos-dados/serie-historica-de-precos-de-combustiveis-e-de-glp) 
    
- Transformação e limpeza dos dados
    - Devido ao considerado numero de dados foi utilizado o scrip "conversao_base.py" para fazer a junção das bases em um unico dataset. 

[!NOTE] Devido ao tamanho considerável da base de dados tratada, ela está disponível por meio do seguinte [link.](https://drive.google.com/open?id=1QwEoQhqSv5kFI47zkgHsD8V0zKkpV37w&usp=drive_fs)


- Carregamento dos dados para um armazenamento estruturado
    - Os dados foram analisados de duas maneira:
            Primeiro foi utilizado a aplicação Power BI para ter um panorama geral dos dados e em seguida feita uma analise detalhada dos dados utilizando o as bibliotecas pandas e matplotlib.

Após a análise exploratória dos dados de combustíveis por região, observamos que:
- A Região Norte apresenta os valores médios mais elevados, com destaque para o estado do Acre, que possui o maior preço médio de combustível entre todos os estados.
- Por outro lado, o estado do Amapá apresenta um valor significativamente abaixo da média regional, o que pode indicar uma possível inconsistência nos dados ou uma anomalia de mercado que merece investigação.
- As demais regiões do país — Sul, Sudeste, Centro-Oeste e Nordeste — mostram preços médios mais homogêneos, com baixa variação entre os estados, sugerindo maior estabilidade nos valores praticados.

## Segunda parte da atividade
Na segunda parte do projeto, foi realizada a análise exploratória dos dados e o treinamento de um modelo de aprendizado de máquina para prever os valores dos combustíveis por região. No entanto, ao analisar os resultados, observamos que o algoritmo não apresentou um desempenho satisfatório, pois as previsões não condizem com os valores reais. Diante disso, será necessário aprimorar o projeto ou optar por outro algoritmo de aprendizado de máquina que ofereça maior precisão.



### Tecnologias Utilizadas
🔹 Power BI 🔹 Jupyter Notebook 🔹 Pandas 🔹 Matplotlib  🔹 Git