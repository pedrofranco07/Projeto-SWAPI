import requests

def obter_planetas():
    url = "https://swapi.dev/api/planets/"
    planetas = []

    while url:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            dados = resposta.json()
            planetas.extend(dados['results'])
            url = dados['next']
        else:
            print("Erro ao buscar planetas")
            return []

    return planetas

r = requests.get("https://swapi.dev/api/people/")

if r.status_code == 200:
    data = r.json()
    personagens = data["results"]

    print("Lista de Personagens:")
    for i, personagem in enumerate(personagens, start=1):
        print(f"{i} - {personagem['name']}")

    escolha = int(input("\nSelecione um personagem pelo número: "))

    if 1 <= escolha <= len(personagens):
        escolhido = personagens[escolha - 1]
        print("\nInformações completas:")
        for key, value in escolhido.items():
            if key == "films":
                print("Filmes:")
                for filme_url in value:
                    filme_response = requests.get(filme_url)
                    if filme_response.status_code == 200:
                        filme_data = filme_response.json()
                        print(f"- {filme_data['title']}")
                    else:
                        print("- Filme não encontrado")
            else:
                print(f"{key.title()}: {value}")
    else:
        print("Número inválido. Escolha entre 1 e 10.")

    planetas = obter_planetas()
    planetas.sort(key=lambda p: int(p['residents'].count(',') + 1 if p['residents'] else 0), reverse=True)

    print("\nPlanetas ordenados pelo número de residentes:")
    for planeta in planetas:
        num_residentes = len(planeta['residents']) if planeta['residents'] else 0
        print(f"{planeta['name']} - {num_residentes} residentes")

else:
    print("Erro na API")
