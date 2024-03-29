# Game of Life

Este projeto é uma implementação do Game of Life ([Jogo da Vida](https://pt.wikipedia.org/wiki/Jogo_da_vida)). Para os que não sabem, é um dos exemplos mais notáveis de autômato celular ([Automato celular](https://pt.wikipedia.org/wiki/Aut%C3%B3mato_celular)).

## Como rodar?

### Baixando o ambiente

Antes de tudo, garanta que o python está instalado na máquina para ser possível rodar o projeto. Caso não tenha, [neste link](https://www.python.org/downloads/) é possível baixá-lo.
Para baixar é muito simples, ou se usa `git clone https://github.com/AHVG/Game-of-Life.git` ou `git clone git@github.com:AHVG/Game-of-Life.git` ou baixa diretamente o zip do projeto. Independete do modo é necessário saber onde foi instalado para ser possível fazer o próximo passo.

### Criando um ambiente virtual

Para uma melhorar experiência, é interessante usar um ambiente virtual do python ([documentação](https://docs.python.org/pt-br/3/tutorial/venv.html)), principalmente para futuramente não dar conflito com as bibliotecas já instalados do python. No link dado, está como é feito isso. Essencialmente é precisso apenas entrar dentro da pasta do projeto, usando `cd ./path/da/pasta/Game-of-Life/`, por exemplo, e criar um ambiente virtual e em seguida ativá-lo com `source nome-do-ambiente-virtual/bin/activate` (esse comando pode variar de SO, veja a documentação para saber qual é o seu).

### Instalando as dependências

Depois de criado e ativado o ambiente virtual, basta executar o pip na raiz do projeto para instalar o requirements.txt. Para isso, use o seguinte comando `pip3 install -r requirements.txt`, para o linux, e `pip install -r requirements.txt`, para o Windows.

### Executando o programa

Finalmente, após ter feito todos passos anteriores, execute os seguintes comandos na raiz do projeto para executá-lo: `cd src/` e, em seguida, `python3 main.py`, para linux, ou `python main.py`, para Windows.

## Como funciona

Ao abrir, estará uma tela onde à esquerda tem as teclas possíveis de serem usados e suas funções e à direita a simulação do Game of Life. A seguir estão imagens do programa.


![image](https://github.com/AHVG/Game-of-Life/assets/97568599/dd1e0cdf-41cf-4fad-b054-f16369f03063)

![image](https://github.com/AHVG/Game-of-Life/assets/97568599/d3baeb27-d1aa-4f93-8f1a-2c9d17592ffb)

![image](https://github.com/AHVG/Game-of-Life/assets/97568599/ee3d8b73-c236-4c54-bb3b-7ffca124d5d0)







