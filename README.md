## Questão 2 - Comandos Docker

a) Construir a imagem:

`docker build -t meu-sistema:1.0 .`

b) Criar e executar o container em segundo plano:

`docker run -d --name sistema-web -p 8080:5000 meu-sistema:1.0`

c) Listar containers em execução:

`docker ps`

d) Ver os logs do container:

`docker logs sistema-web`

e) Parar o container:

`docker stop sistema-web`

f) Remover o container:

`docker rm sistema-web`

## Questão 3 - Entendendo o Docker

**a) Diferença entre imagem e container**

A imagem Docker é um modelo somente leitura, formado por camadas, que contém o sistema de arquivos, as dependências, o código da aplicação e as instruções de execução. Ela por si só não executa nada. O container é uma instância criada a partir de uma imagem, que está em execução (ou parada) como um processo isolado e com uma camada gravável por cima da imagem. A partir de uma mesma imagem é possível criar vários containers.

**b) Por que a alteração no app.py não apareceu**

O arquivo `app.py` foi copiado para dentro da imagem no momento do `docker build` (instrução `COPY . .`). A imagem é imutável, então ela continua com a versão antiga do arquivo, e todo container criado a partir dela usa o código antigo. Editar o arquivo na máquina não altera a imagem.

Para executar a versão atualizada, o aluno precisa:

1. Reconstruir a imagem: `docker build -t meu-sistema:1.0 .`
2. Parar o container antigo: `docker stop sistema-web`
3. Remover o container antigo: `docker rm sistema-web`
4. Criar um novo container a partir da imagem reconstruída: `docker run -d --name sistema-web -p 8080:5000 meu-sistema:1.0`
