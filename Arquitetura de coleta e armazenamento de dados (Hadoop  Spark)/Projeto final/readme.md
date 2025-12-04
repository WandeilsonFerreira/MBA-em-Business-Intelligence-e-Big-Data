# Laboratório 03: Carregando Dados no HDFS para o Hive

Olá\! Neste laboratório, nosso objetivo é preparar o ambiente para que o Apache Hive possa consultar nossos dados. O processo envolve três grandes etapas:

1.  **Iniciar nosso ambiente** de Big Data com Docker.
2.  **Copiar os dados** do nosso computador para dentro do ambiente.
3.  **Mover os dados** para o HDFS, o sistema de arquivos que o Hadoop e o Hive utilizam.

Vamos começar\!

-----

### Passo 1: Iniciar o Ambiente Hadoop/Hive

Primeiro, precisamos "ligar" nosso cluster Hadoop e o serviço do Hive. Usaremos o Docker Compose para orquestrar e iniciar todos os contêineres necessários de uma só vez.

##### Comando 1.1: Navegar até a pasta de configuração

```bash
cd lab-03-resources/hadoop/hive
```

  * **O que faz?** O comando `cd` (Change Directory) nos leva para a pasta `lab-03-resources/hadoop/hive`.
  * **Por que fazemos isso?** É nesta pasta que se encontra o arquivo `docker-compose.yml`. Este arquivo é a "receita" que o Docker usa para saber quais serviços (contêineres) ele deve criar e como eles devem se comunicar. Precisamos estar no mesmo diretório que ele para executá-lo.

##### Comando 1.2: Iniciar os serviços com Docker Compose

```bash
docker-compose up -d
```

*(Observação: O comando correto é `docker-compose` e não `docker composer`)*

  * **O que faz?** Este comando lê o arquivo `docker-compose.yml` e inicia todos os serviços definidos nele (como o NameNode e DataNode do HDFS, o Metastore e o Server do Hive, etc.). A opção `-d` (de *detached*) faz com que tudo rode em segundo plano, liberando seu terminal.
  * **Por que fazemos isso?** Este é o passo que efetivamente cria nosso ambiente de Big Data. Ao final dele, teremos um "mini-cluster" Hadoop rodando em nossa máquina, pronto para receber dados.

Após esse passo você conseguirá acessar as seguintes aplicações:

| Porta     | Serviço / Componente                          | Uso principal                                |
| --------- | --------------------------------------------- | -------------------------------------------- |
| **10000** | HiveServer2                                   | Conexão JDBC/ODBC do Hive                    |
| **10002** | Possível Web UI do HiveServer2 ou Beeline web | Monitorar queries Hive (depende do setup)    |
| **19888** | **MapReduce JobHistory Server**               | Histórico de jobs finalizados do MapReduce   |
| **8042**  | NodeManager UI (YARN)                         | Métricas e logs por nó do cluster            |
| **8088**  | **YARN ResourceManager UI**                   | Status de jobs em execução e fila do cluster |
| **9083**  | Hive Metastore Service                        | Metastore do Hive                            |
| **9820**  | Pode ser HBase Master UI                      | Admin HBase                                  |
| **9870**  | HDFS NameNode UI                              | Estado e navegação no HDFS                   |


-----

### Passo 2: Transferir os Dados para o Ambiente

Nosso ambiente está rodando, mas ele está isolado dentro de contêineres Docker. Precisamos agora transferir nossos arquivos de dados (os `.csv`) do nosso computador local para dentro de um desses contêineres.

##### Comando 2.1: Acessar a pasta com os dados

```bash
cd ./lab-03-resources/data
# Se você executou o passo anterior, o caminho relativo seria: cd ../../data
```

  * **O que faz?** Usamos o `cd` novamente para navegar até a pasta onde nossos arquivos de dados, como `categories.csv`, estão localizados.
  * **Por que fazemos isso?** O próximo comando precisa "enxergar" o arquivo que queremos copiar. Estar na mesma pasta simplifica o caminho do arquivo.

##### Comando 2.2: Copiar o arquivo para dentro do contêiner

```bash
docker cp categories.csv hive:/tmp/
```

  * **O que faz?** O comando `docker cp` copia arquivos entre o seu computador (host) e um contêiner Docker.
      * `categories.csv`: É o arquivo de **origem** no seu computador.
      * `hive:/tmp/`: É o **destino**. `hive` é o nome do nosso contêiner de serviço do Hive, e `/tmp/` é uma pasta temporária dentro dele.
  * **Por que fazemos isso?** Este é o "portal" para levar dados para dentro do nosso ambiente. O arquivo agora existe dentro do contêiner, mas ainda não está no HDFS.

-----

### Passo 3: Mover os Dados para o HDFS

Com o arquivo `categories.csv` dentro do contêiner, o último passo é colocá-lo no **Hadoop Distributed File System (HDFS)**. O HDFS é o sistema de armazenamento distribuído que o Hive utiliza para ler os dados de forma performática.

##### Comando 3.1: Criar uma pasta no HDFS

```bash
hdfs dfs -mkdir -p /user/hive/warehouse/categories
```

*(Nota: Este comando é executado de dentro do contêiner ou através de uma interface que tenha acesso ao HDFS)*

  * **O que faz?**
      * `hdfs dfs`: É o conjunto de ferramentas para interagir com o HDFS.
      * `-mkdir`: É o comando para criar um diretório (uma pasta).
      * `-p`: Garante que todos os diretórios pais no caminho (`/user/hive/warehouse/`) sejam criados caso ainda não existam.
      * `/user/hive/warehouse/categories`: É o caminho completo da pasta que estamos criando dentro do HDFS.
  * **Por que fazemos isso?** É uma boa prática organizar os dados no HDFS em pastas que correspondam às tabelas que criaremos no Hive posteriormente. Isso mantém nosso data warehouse limpo e organizado.

##### Comando 3.2: Mover o arquivo para a pasta no HDFS

```bash
hdfs dfs -put /tmp/categories.csv /user/hive/warehouse/categories/
```

  * **O que faz?**
      * `hdfs dfs -put`: É o comando para copiar arquivos do sistema de arquivos local (do contêiner, neste caso) para o HDFS.
      * `/tmp/categories.csv`: É a **origem** do arquivo, o local onde o colocamos no Passo 2.2.
      * `/user/hive/warehouse/categories/`: É o **destino**, a pasta que acabamos de criar no HDFS.
  * **Por que fazemos isso?** Este é o passo final\! Agora, os dados do arquivo `categories.csv` estão oficialmente armazenados no HDFS e prontos para serem mapeados por uma tabela no Hive.

-----

## Sua Vez\! 

Você aprendeu o fluxo completo para carregar um arquivo no HDFS\! O processo é sempre o mesmo:

1.  **Copiar o arquivo local para o contêiner:** Use `docker cp`.
2.  **Criar a pasta correspondente no HDFS:** Use `hdfs dfs -mkdir -p`.
3.  **Mover o arquivo do contêiner para a pasta no HDFS:** Use `hdfs dfs -put`.

Agora, repita esse processo para os outros arquivos de dados do laboratório:

  * `customers.csv`
  * `employees.csv`
  * `employee-territories.csv`
  * `orders.csv`
  * `order-details.csv`
  * `products.csv`
  * `regions.csv`
  * `shippers.csv`
  * `suppliers.csv`
  * `territories.csv`


Lembre-se de criar uma pasta específica no HDFS para cada um deles\! Bom trabalho\!

## Ajustar permissões da pasta no HDFS
Isso garante que qualquer usuário possa criar e entrar nessas pastas (igual ao /tmp em sistemas Linux).

```bash
hdfs dfs -chmod -R 1777 /tmp
hdfs dfs -chmod -R 1777 /tmp/hadoop-yarn/staging
```

## Extra

Arquivos maiores de 128MB
> https://drive.google.com/drive/folders/1q_1dj1mWqQX4m9surb46Ku-YdLtiKHuM?usp=drive_link
ou
> https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews/data