# GLOBAL-SOLUCTION---PYTHON

Consultor de Carreira Inteligente com IA + Base de Conhecimento
📌 Sobre o Projeto

Este projeto é um assistente inteligente de orientação de carreira, desenvolvido para unir agilidade de consulta a dados estruturados com o poder da IA generativa.

Ele opera em dois modos complementares:

🔍 1. Consulta à Base de Conhecimento Local (JSON)

O software verifica primeiro um arquivo dados.json, onde ficam armazenadas áreas profissionais, competências relevantes, tendências e roadmaps curados manualmente.

Assim, quando o usuário busca uma área conhecida, a resposta é imediata, offline e altamente confiável.

🤖 2. Geração via Inteligência Artificial (Google Gemini)

Se a profissão não existir no banco local, o sistema automaticamente aciona a API do Google Gemini, gerando uma análise completa em tempo real, contendo:

Principais skills técnicas e comportamentais

Roadmap de estudo passo a passo

Sugestões de portfólio

Tecnologias essenciais da área

Isso garante que o sistema esteja sempre atualizado com o mercado.

🚀 Principais Funcionalidades

📚 Pesquisa inteligente com fallback automático (JSON → IA)

⚡ Respostas rápidas para áreas conhecidas

🧩 Estrutura modular para expansão de novas áreas

🌐 Integração nativa com Google Generative AI

📝 Retorno organizado e pronto para uso em relatórios, sites ou apresentações

🛠️ Requisitos

Para executar o projeto, você precisará de:

Python 3+

Biblioteca Google Generative AI

Uma Google API KEY válida
(criada no console Google AI)

📦 Instalação das Dependências

No terminal, instale o SDK do Gemini:

pip install google-generativeai
