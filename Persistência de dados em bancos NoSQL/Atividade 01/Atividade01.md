# MongoDB

## Consultas básicas

### Encontre todos os concursos onde houve acumulo de prêmio
```
db.loteria.find({
	Acumulado: { $eq: "SIM" }}),
	{Concurso: 1, Arrecadacao_Total: 1}
	).sort({ Valor_Acumulado: -1 })
```

###  Liste os 10 concursos com maior arrecadação
```
db.loteria.find(
	{Arrecadacao_Total: { $gt: 0}},
	{ Concurso:1, Arrecadacao_Total: 1, _id:0 }
	).sort({Arrecadacao_Total: -1}).limit(10)
```

### Encontre os concursos onde não houve ganhadores da sena
```
db.loteria.find(
  	{ Ganhadores_Sena: { $eq: 0 } },
  	{ Concurso: 1, Ganhadores_Senal: 1, _id: 0 }
)
```

### Verificando o numero de concursos sem ganhadores
```
db.loteria.find(
  	{ Ganhadores_Sena: { $eq: 0 } },
  	{ Concurso: 1, Ganhadores_Senal: 1, _id: 0 }
	).count()
```

## Consultas com agregação
### Calcule a média de arrecadação por estado (UF)
```
 db.loteria.aggregate([
 	{ $group: { 
		_id: "$UF", 
		total_arrecadado: { $sum: "$Arrecadacao_Total" },
		media_arrecadacao: { $avg: "$Arrecadacao_Total" }
	}},
 	{ $sort: { total_arrecadado: -1 } }
 	])
```

### Encontre os 10 números mais sorteados em todos os concursos
```
 db.loteria.aggregate([
 { $project: { 
		numeros: { $concatArrays: [
		["$1ª Dezena"], ["$2ª Dezena"], ["$3ª Dezena"],
		["$4ª Dezena"], ["$5ª Dezena"], ["$6ª Dezena"]
		]} 
}},
 { $unwind: "$numeros" },
 { $group: { _id: "$numeros", total: { $sum: 1 } } },
 { $sort: { total: -1 } },
 { $limit: 10 }
 ])


```
### Identifique quais cidades tiveram mais ganhadores da sena
```
 db.loteria.aggregate([
 	{ $group: { 
		_id: "$Cidade", 
		Ganhadores_Sena: { $sum: "$Ganhadores_Sena" },		 
	}},
 	{ $sort: { Ganhadores_Sena: -1 } }
 	])
```

## Análise temporal
### Crie uma análise mensal da arrecadação total
```
db. loteria. aggregate([
	{
		$addFields: {
			Mes: { $month: "$Data Sorteio" },
			Ano: { $year: "$Data Sorteio" }
			}
		},		 
		{
		$group: {
			_id: { ano: "$Ano", mes: "$Mes" },
			Total_Arrecadado: { $sum: "$Arrecadacao_Total" },
			Total_Acumulado: {
				$sum: {
					$cond: [ { $eq: ["$Acumulado", "SIM"] }, "$Valor_Acumulado", 0 ]
					}
				},

		Sorteios_Acumulados: {
			$sum: {
				$cond: [ { $eq: ["$Acumulado", "SIM"] }, 1, 0 ]
			}
		},
		
		Total_Sorteios: { $sum: 1 }
			} 
		},
		{ 
		$sort: { "_id.ano": 1, "_id.mes": 1 }
	}		
])
```
### Verifique se há tendências sazonais nos prêmios acumulados
Apresenta as variações sazonais — ou seja, se há meses ou épocas do ano em que os prêmios acumulados tendem a ser maiores ou menores.
```
db.loteria.aggregate([
  {
    $addFields: {
      mes: { $month: "$Data_Sorteio" },
      ano: { $year: "$Data_Sorteio" }
    }
  },
  {
    $group: {
      _id: "$mes",
      media_acumulado: { $avg: "$Valor_Acumulado" },
      total_acumulado: { $sum: "$Valor_Acumulado" },
      sorteios: { $sum: 1 }
    }
  },
  {
    $sort: { _id: 1 }
  }
])
```
### Calcule a média móvel de 6 meses para o valor acumulado
```
db.sorteios.aggregate([
  {
    $addFields: {
      ano: { $year: "$Data_Sorteio" },
      mes: { $month: "$Data_Sorteio" },
      semestre: {
        $cond: [
          { $lte: [{ $month: "$Data_Sorteio" }, 6] },
          1,
          2
        ]
      }
    }
  },
  {
    $group: {
      _id: { ano: "$ano", semestre: "$semestre" },
      media_acumulado_6m: { $avg: "$Valor_Acumulado" },
      total_sorteios: { $sum: 1 }
    }
  },
  {
    $sort: { "_id.ano": 1, "_id.semestre": 1 }
  }
])
```

## Estatísticas avançadas
### Calcule a probabilidade de cada número ser sorteado
```
```
### Identifique combinações de números que aparecem juntos com frequência
```
```
### Analise a correlação entre arrecadação e número de ganhadores
```
```
## Preparação para visualização
### Crie visualizações para os números mais sorteados
```
```
### Prepare dados para um gráfico temporal da arrecadação
```
```
### Gere dados para um mapa de ganhadores por estado
```
```
