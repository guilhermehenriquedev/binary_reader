
# ECHI CONVERTER

Aplicação para leitura, conversão e inserção de códigos binários (bilhetes) em um banco de dados,
contendo API REST para vizualização e execução de ações.

# Requerimentos e configuração
Para utilizar os recursos da aplicação é nescessário ter instalado as tecnologias [Python][], [Django][] e suas dependencias, com base nisso, siga os passos abaixo para configuração e instalação dos recursos

[Python]: https://docs.python.org/3/
[Django]: https://docs.djangoproject.com/en/4.0/

## Funcionalidades:

- [x] Ler arqvuios contendo binários e converte-los
- [x] Gravar registros em banco de dados
- [x] Aprensentar registros ou executar ações por meio de API REST

## Instalação e configuração

* 1º Clone o repositório em sua máquina:

```bash
git clone git@gitlab.com:telesul_sistemas/ech.git
```


* 2º Para fluidez e garantia que o projeto irá funcionar perfeitamente é necessário ter a versão do Python 3.10.0 instalado na sua máquina

* 3º Agora você irá precisar do instalador de pacotes [Pip][], para isso digite o comando:

[Pip]: https://docs.python.org/3/

```bash
sudo apt install python3-pip
```

Seguindo os passos acima você já tem o essencial para instalação de dependencias e configuração de ambiente da aplicação

# Instalando dependencias 

Antes de instalar as dependencias do projeto, precisamos de um ambiente virtual. Para isso digite no seu terminal o seguinte comando:

```bash
python3 -m venv venv
```
Irá ser criado automaticamente um arquivo com seu ambiente virtual

Após isso, crie um arquivo .env, e coloque nele as seguintes variáveis conforme exemplo abaixo:
```bash
DB_HOST="cole aqui o IP do seu banco de dados"
DB_NAME="ech"
DB_USER="SeuUsuárioDoBancoDeDados"
DB_PASS="SuaSenhaDoBancoDeDados"
ALLOWED_HOSTS=*
DIRECTORY_FILE="cole aqui o caminho da pasta onde os arquivos dos bilhetes estão"
DIRECTORY_HISTORY="cole aqui o caminho da pasta onde os arquivos processados ficarão"
```

Após isso, ative seu ambiente virtual com o comando:

```bash
source venv/bin/activate
```
Agora iremos instalar as dependecias necessárias para que o projeto possa funcionar corretamente, com o comando:

```bash
pip install -r requirements.txt
```
Execute o comando abaixo para aplicar migrações e manipulações do esquema de banco de dados do Django:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Agora você pode executar seu servidor local, caso queira consumir as API's, com o comando abaixo:

```bash
python3 manage.py runserver
```

Será gerado o ip na qual a API irá executar na web, no caso http://127.0.0.1:8000

Copie o ip gerado e cole na url do navegador da seguinte forma http://127.0.0.1:8000/api

# Urls
Abaixo você verá as urls disponíveis na aplicação e suas finalidades

* http://127.0.0.1:8000/api/records/ = Busca todos os registros do banco de dados echi_records
* http://127.0.0.1:8000/api/records/echi_convert/ = Executa a leitura, conversão e inserção dos bilhetes 


# Sistema de logs
A cada execução no sistema, será gerado um registro de log no arqvuivo "log/application.log"
