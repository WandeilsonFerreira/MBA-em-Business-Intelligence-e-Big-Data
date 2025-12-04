# Algorítmos de Mineração de Dados e Web Mining e Web Semântica
## Descrição do projeto
Este projeto faz parte das atividades do MBA em Business Intelligence e Big Data, e tem como objetivo a criação de um modelo preditivo utilizando Regressão Logística para prever a sobrevivência dos passageiros do Titanic.
## Tecnologias utilizadas
- Python
- Pandas
- NumPy
- Matplotlib e Seaborn
- Scikit-learn
## Etapas desenvolvidas
### Etapa 1: Coleta de dados
	# Importando as bibliotecas
	import numpy as np
	import matplotlib.pyplot as plt
	import pandas as pd

	from sklearn.model_selection import train_test_split
	from sklearn.preprocessing import StandardScaler
	from sklearn.linear_model import LogisticRegression
	from sklearn.metrics import confusion_matrix
	import seaborn as sns	
	import matplotlib.pyplot as plt

	print(pd.__version__)
	print(np.__version__)
	
	# Carregando os dados
	titanic = pd.read_csv("/content/titanic.csv")
	titanic.head()
	
	# Apresentar informações estatísticas descritivas do conjunto de dados
	titanic.describe()	
	

### Etapa 2: Análise Exploratória de Dados (Tratamento de dados)
	# Analise do numero de sobreviventes
	distribution = sns.countplot(x='survived', data = titanic)
	
	# Apagando os atributos que não interessam a modelagem
	colunas_deletadas = ['name', 'ticket','cabin']
	titanic = titanic.drop(colunas_deletadas, axis=1)
	titanic.head()
	
	# Resolver valores ausentes - Missing Values
		print('-- Antes do tratamento --')
		print(titanic.isnull().sum())
		print(titanic['pclass'].count())
		Realizar a exclusão dos registros com valores ausentes b
		titanic = titanic.dropna()
		print('-- Depois do tratamento --')
		titanic = titanic.dropna()
		print(titanic.isnull().sum())
		print('-- Informações sobre o dataset --')
		titanic.info()

### Etapa 3: Modelagem 
	# Substituindo os valores categóricos (nominais) por valores numéricos
	titanic = pd.get_dummies(titanic)
	
	# Usando o método loc com lógica booleana. Pegando todas as colunas diferentes de "survived"
	from IPython.display import display	
	X = titanic.loc[:,titanic.columns!="survived"].values
	y = titanic.iloc[:, 5].values
	display(X)
	display(y)	
	
	# Separação do dataset em treinamento e tests
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30,random_state=0)													

	# Feature Scaling - Normalização
	sc_X = StandardScaler()
	X_train = sc_X.fit_transform(X_train)
	X_test = sc_X.transform(X_test)
	display(X_train)
	display(X_test)
	
	# Parametros para o classificador random_state=0 e solver='lbfgs'
	from sklearn.linear_model import LogisticRegression
	classifier = LogisticRegression()

	# Trainando o modelo
	classifier.fit(X_train, y_train)

	# Prevendo alguns valores com o conjunto de dados de teste
	y_pred = classifier.predict(X_test)
	y_pred

### Etapa 4: Avaliação
	# Criando uma Matriz de Confusão para analisar o resultado da previsão feita pelo modelo
	# Making the confusion Matrix
	from sklearn.metrics import confusion_matrix
	cm = confusion_matrix(y_test, y_pred)
	cm
	
  	# Verificando a acurácia do modelo utilizado
	from sklearn.metrics import accuracy_score

	for clf in (classifier,):
		clf.fit(X_train, y_train)
		y_pred = clf.predict(X_test)
		print(clf.__class__.__name__, accuracy_score(y_test, y_pred))
## Resultados
A acurácia do modelo de Regressão Logística para o conjunto de teste é de aproximadamente 82,11%. Isso significa que o modelo está correto em 82,11% das previsões sobre a sobrevivência dos passageiros do Titanic.
## Conclusões
Os resultados obtidos, com uma acurácia de aproximadamente 82,11%, demonstram a eficácia do modelo de Regressão Logística em prever a sobrevivência dos passageiros do Titanic, fornecendo uma visão valiosa sobre os fatores que influenciaram a sobrevivência. Este projeto não apenas reforça as habilidades técnicas dos alunos em Machine Learning e análise de dados, mas também destaca a importância do rigor metodológico e da atenção aos detalhes em todo o processo de desenvolvimento de modelos preditivos.
