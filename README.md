## Projeto - Web Crawler

- Desenvolvedores: Severino Urtiga

### Tecnologias utilizadas:

- Python
- Scrapy
- Shell
- MySql
- Pandas
- Matplotlib
- Docker
- Git

## Descrição do Projeto

- Esse projeto é um processo de web crawling e tem como objetivo coletar dados de portais concorrentes de notícias, agregar métricas sobre esses dados e disponibilizar informações. Foi usado no projeto dados de noticias dos portais Tecnoblog, Canaltech, TechMundo e Techtudo.

## Primeiros passos

- Primeiramente tenha o <b>Python</b> instalado em sua máquina.

- Instale a venv com o comando <b>sudo apt install python3-venv</b> em seu terminal.
 
- Em seguida, execute o comando <b>python3 -m venv .venv</b> em seu terminal para criar o ambiente virtual.

- Depois, execute o comando <b>source .venv/bin/activate</b> para ativar o ambiente.

- Para build, execute o comando <b>pip install -r requirements.txt</b> para baixar todas as depêndencias do projeto.

- Clone o projeto dentro de um diretório de sua preferencia. <b>git clone </b>
  
  
## Após o build do projeto, iremos subir o container do MySql(Banco de Dados) no Docker.

- Primeiramente tenha o <b>Docker</b> instalado em sua máquina.
  
- Execute o docker-compose.yml com o comando <b>docker-compose up -d</b> isso ira criar e subir o banco de dados Mysql.

- Após isso acesse o banco de dados no endereço http://localhost:8081, <b>servidor:mysql</b> - <b>user:root</b> - <b>pass:example</b>
  
  
## Executando a carga

- Após a etapa anterior iremos executar a carga dos dados no banco, entre no diretorio do projeto e execute o shell script com o comando <b>./carga.sh</b>.

- Quando finalizar é possível ver os dados no mysql. 



## Observações: Pontos de melhorias futuras para serem desenvolvidos

- Uso das bibliotecas do Python para análise de dados <b>pandas</b> e <b>matplotlib</b>.

- Uso de <b>jupyter notebook</b> para auxiliar nas análises.

- Implementação de métricas para dados estruturado como:
1. Quantidade;
2. Métricas derivadas do texto;
3. Alguma métrica de engajamento.
