import requests
from bs4 import BeautifulSoup

def extrair_resultados(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Erro ao fazer a requisição:", e)
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    sorteio = 0

    # Extrai os dados dos resultados
    resultados = []
    for div in soup.find_all('div', {'class': 'col-12 col-md-12 bg-cinza-claro shadow-smclaro p-2 text-center'}):
        sorteio = sorteio + 1 
        titulo = str(sorteio) + "o. Sorteio"
        
        # Extraindo os valores dos spans
        numeros = [int(span.text.strip()) for span in div.find_all('span', {'class': 'rounded-circle bg-bola shadow-sm p-2 mt-2 font-weight-bold'})]

        resultado = {
            'titulo': titulo,
            'numeros': numeros
        }
        resultados.append(resultado)

    return resultados


if __name__ == "__main__":
    url = "https://www.trimania.com.br/vale/?DtSorteio=2021-05-23&ordem=bola#resultado"
    resultados = extrair_resultados(url)
    if resultados:
        print("Resultados extraídos com sucesso!")
        for resultado in resultados:
            print(f"{resultado['titulo']}: {', '.join(str(num) for num in resultado['numeros'])}")
    else:
        print("Não foi possível extrair os resultados.")
