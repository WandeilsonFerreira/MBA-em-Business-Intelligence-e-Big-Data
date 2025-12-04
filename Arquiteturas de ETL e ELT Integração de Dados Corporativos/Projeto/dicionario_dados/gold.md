# Dicionário de Dados: European Soccer Database
Este banco de dados reúne informações detalhadas sobre o futebol europeu, ideal para análises e machine learning. Ele contém estatísticas de mais de 25.000 partidas e 10.000 jogadores, além de atributos retirados do jogo FIFA da EA Sports. Também inclui dados de apostas, eventos das partidas e formações dos times, cobrindo 11 países e as temporadas de 2008 a 2016.

## Camada Gold
 
## Descrição
A camada **Gold** representa dados refinados e estruturados para análise de desempenho dos times ao longo das temporadas. As colunas listadas abaixo agregam métricas de gols, eficiência ofensiva e defensiva, permitindo uma avaliação comparativa entre as equipes.

## Estrutura da Tabela

| Nome da Coluna           | Tipo    | Descrição |
|--------------------------|--------|-----------|
| `ano`                   | STRING  | Ano da temporada |
| `time_casa_api_id`       | INTEGER | Identificador do time mandante |
| `team_long_name`         | STRING  | Nome completo do time |
| `gols_time_casa`         | INTEGER | Número de gols marcados pelo time mandante |
| `gols_time_visitante`    | INTEGER | Número de gols marcados pelo time visitante |
| `media_gols`            | FLOAT   | Média de gols por partida do time mandante |
| `media_gols_fora_de_casa` | FLOAT  | Média de gols por partida do time visitante |
| `total_shots_on_target`  | INTEGER | Número total de finalizações certas do time mandante |
| `avg_goals_conceded`     | FLOAT   | Média de gols sofridos pelo time na temporada |

---

##  Objetivo da Camada Gold
- **Facilitar análises avançadas** sobre o desempenho dos times por temporada.  
- **Comparar eficiência ofensiva e defensiva** para identificar padrões de desempenho.  
- **Fornecer insights para modelos preditivos** relacionados ao futebol.  