# GLOBAL-SOLUCTION---PYTHON

Descrição do Projeto

O software atua como um consultor de carreira inteligente. Ele opera em dois modos:

1.  Busca em Base de Conhecimento (JSON): Primeiramente, o sistema verifica um arquivo local (`dados.json`) que contém informações curadas sobre áreas de atuação e suas evoluções.

2.  Geração via Inteligência Artificial: Caso a profissão não seja encontrada no banco de dados local, o sistema se conecta à API do Google Gemini para gerar, em tempo real, uma análise completa contendo skills, roadmap de aprendizado e dicas de portfólio.

Requisitos e Dependências

Para executar este projeto, você precisará de:

Python 3 para cima instalado.
Biblioteca Google Generative AI
Google API KEY


Instalação das dependências

Execute o comando abaixo no seu terminal para instalar o SDK do Google:
pip install google-generativeai
