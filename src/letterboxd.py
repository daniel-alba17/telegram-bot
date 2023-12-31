import logging
import requests
from bs4 import BeautifulSoup
import json


BASEURL = "https://letterboxd.com/"


class LetterBoxd:
    @staticmethod
    def get_watchlist(usernames=["daniel_alba", "malejaa"]):
        result_global = []
        for username in usernames:
            result = []
            page = 1
            max_pages = 1
            print("======USERNAME", username)
            while page <= max_pages:
                print("paginas", page)
                print("maximo de plaginas", max_pages)
                response = requests.get(f"{BASEURL}{username}/watchlist/page/{page}")

                # Verifica si la solicitud fue exitosa (código de estado 200)
                if response.status_code == 200:
                    # Parsea el contenido HTML con BeautifulSoup
                    soup = BeautifulSoup(response.text, "html.parser")

                    ul_element = soup.find("ul", class_="poster-list")
                    pagination = soup.find("div", class_="pagination")
                    max_pages = len(pagination.find_all("li"))
                    # print(ul_element)

                    # Verifica si se encontró el elemento
                    if ul_element:
                        # Obtiene todos los elementos dentro del <ul>
                        lista_de_elementos = ul_element.find_all("img", class_="image")
                        # print(len(lista_de_elementos))

                        # Imprime o manipula los elementos según tus necesidades
                        for elemento in lista_de_elementos:
                            result.append(elemento.get("alt"))
                            pass

                    else:
                        print("No se encontró el <ul> con la clase 'poster-list'.")

                    page += 1

                else:
                    print(
                        "Error al realizar la solicitud HTTP. Código de estado:",
                        response.status_code,
                    )

            result_global.append(result)

        set1 = set(result_global[0])
        set2 = set(result_global[1])

        coincidencias = set1.intersection(set2)

        lista_coincidencias = list(coincidencias)

        return lista_coincidencias
