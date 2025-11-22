"""
ALUNOS: 

Gustavo Almeida Ferreira / RM566980 

Lucas de Oliveira Miranda Caetano / RM568036 

Sofia Souza Rodrigues / RM566708
"""


import google.generativeai as genai
import json

# --- Leitura inicial do arquivo JSON ---
# O arquivo contém todas as áreas, descrições e roadmaps que serão usados
# para responder rapidamente, sem precisar chamar a IA toda vez.
with open("dados.json", "r", encoding="utf-8") as dado:
    DATA = json.load(dado)


def buscar_area(escreve):
    """
    Faz uma busca simples pela área correspondente no JSON.
    A comparação é feita em letras minúsculas para evitar erro por acentuação ou caixa.
    """
    escreve = escreve.lower().strip()

    for area in DATA["areas"]:
        nome_area = area["area"].lower()
        if escreve in nome_area:
            return area

    # Se nada for encontrado, retorna None mesmo.
    return None


def formatar_area_para_texto(area):
    """
    Recebe o dicionário da área encontrada e monta um texto organizado.
    Esse texto será mostrado diretamente para o usuário.
    """

    texto = ""

    texto += f"=== {area['area']} ===\n\n"

    texto += "Descrição:\n"
    texto += f"{area['description']}\n\n"

    texto += "Habilidades Atuais:\n"
    for skill in area["current_skills"]:
        texto += f"- {skill}\n"
    texto += "\n"

    texto += "Profissões do Futuro:\n"
    for prof in area["future_professions"]:
        texto += f"\n## {prof['title']} ##\n"
        texto += "Roadmap:\n"
        for etapa in prof["roadmap"]:
            texto += f"• {etapa}\n"
        texto += "\n"

    return texto


def gerar_texto_streaming(prompt):
    """
    Envia o prompt para o Gemini e exibe a resposta conforme ela é gerada.
    Esse streaming evita aquela espera longa até o texto final ficar pronto.
    """

    GOOGLE_API_KEY = "AIzaSyBm9Gjmr1jKXi83LeiI0vlRtDR6u2YkD6U"
    genai.configure(api_key=GOOGLE_API_KEY)

    modelo = genai.GenerativeModel("gemini-pro-latest")

    # Solicita a resposta já em modo streaming.
    resposta_stream = modelo.generate_content(prompt, stream=True)

    texto_final = ""

    print("\n=== Resposta gerada por IA ===\n")

    # Conforme a IA vai enviando os pedaços da resposta, mostramos na tela.
    for chunk in resposta_stream:
        if chunk.text:
            print(chunk.text, end="", flush=True)
            texto_final += chunk.text

    print("\n\n=== Fim da resposta ===\n")

    return texto_final


def processar_input_usuario(texto):
    """
    Função principal:
    - Primeiro tenta localizar a profissão/área dentro do JSON.
    - Se achar, retorna o conteúdo estruturado.
    - Se não achar, chama a IA para gerar um texto completo do zero.
    """

    resultado = buscar_area(texto)

    if resultado:
        texto_formatado = formatar_area_para_texto(resultado)

        return {
            "status": "encontrado",
            "origem": "banco_de_dados",
            "dados_brutos": resultado,
            "texto_formatado": texto_formatado
        }

    else:
        # Quando não encontra no JSON, prepara o prompt para a IA.
        cargo = texto

        prompt = (
            f"Receba a profissão {cargo} e retorne um texto contendo: "
            f"as skills atuais, as skills futuras necessárias para requalificação caso a profissão seja "
            f"potencialmente substituída; um roadmap objetivo com etapas claras e sequenciais; e, ao final, "
            f"dicas práticas do que incluir no portfólio para essa profissão. Além disso, não inclua caracteres como hashtags ou asteristicos"
        )

        # Agora chamamos diretamente a IA, sem try/except
        texto_gerado = gerar_texto_streaming(prompt)

        return {
            "status": "gerado",
            "origem": "ia",
            "texto_formatado": texto_gerado
        }


entrada = input("Qual a sua profissão atual? ")

resp = processar_input_usuario(entrada)

print("RETORNO FINAL DO PROCESSO:\n")
print(resp["texto_formatado"])
