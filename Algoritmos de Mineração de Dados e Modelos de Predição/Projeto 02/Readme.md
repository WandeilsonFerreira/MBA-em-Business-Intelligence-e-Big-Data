# Algorítmos de Mineração de Dados e Web Mining e Web Semântica
## Descrição do projeto
Este projeto faz parte das atividades do MBA em Business Intelligence e Big Data e tem como objetivo utilizar o conjunto de dados de Recursos Humanos (HR) para treinar um modelo de detecção de anomalias que possa identificar discrepâncias no processo de avaliação dos colaboradores
## Tecnologias utilizadas
- Python
- Pandas
- NumPy
- Matplotlib e Seaborn
- Scikit-learn
## Etapas desenvolvidas
### Etapa 1: Coleta de dados 
    # Importando as bibliotecas
    import pandas as pd
    import numpy as np
    from sklearn.preprocessing import LabelEncoder     
    import plotly.express as px
    import matplotlib.pyplot as plt
    import seaborn as sns
    from pyod.models.iforest import IForest

    print(pd.__version__)
    print(np.__version__)

    # Carregando os dados
    hr = pd.read_csv('HR.csv')

### Etapa 2: Análise Exploratória de Dados (Tratamento de dados)
    # Apresentar informações estatísticas descritivas do conjunto de dados
    hr.head()
    hr.describe().T
    #Verificando valores ausentes
    print(hr.isnull().sum())
    hr.shape
    hr.info()
    hr.columns = hr.columns.str.upper()
    hr.columns

    # CRIANDO UMA INSTÂNCIA DA CLASSE LabelEncoder do sci-kit learn
    labelencoder = LabelEncoder()

    # Assigning numerical values and storing in another column
    hr['SALES'] = labelencoder.fit_transform(hr['SALES'])

    # Assigning numerical values and storing in another column
    hr['SALARY'] = labelencoder.fit_transform(hr['SALARY'])

    hr.head()


### Etapa 3: Modelagem de Detecção de Anomalias 
    """ Detecção de Outliers de forma visual"""

    fig = px.scatter(hr,
                    x='LAST_EVALUATION',
                    y='AVERAGE_MONTLY_HOURS',
                    color='LEFT',
                    color_discrete_sequence=px.colors.qualitative.Antique
                    )
    fig.show()

    """ Aplicação do modelo IsolationForeset para Deteção de Anomalias"""   
    fig = px.box(hr,
                y = 'SATISFACTION_LEVEL')
    fig.show()

    # classificação de quem é outliers ou não
    outliner_detection_clf = IForest(contamination=0.05, #Porcentagem de outliers que desejamos encontrar na amostra
                                random_state = 42,
                                verbose=True)

    # Contando os outliers
    n_outliers = np.count_nonzero(y_pred ==1)

    print(f'\nExistem {n_outliers} outliners dentro dessa amostra\n')
    #print("número de outliders:", n_outliers)

    # Mostrar a quantidade de outliers e não outliers
    #np.unique(y_pred, return_counts=True)

    out = hr.loc[hr['OUTLIERS'] == 1]
    print(f'Quantidade de outliers: {(len(out))}')

    y_pred


### Etapa 4: Avaliação
    # Criando uma nova coluna para classificação dos outliers (0 = inliders, 1 = outliers).
    hr['OUTLIERS'] = y_pred.tolist()
