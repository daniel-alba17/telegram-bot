import logging
import requests
from bs4 import BeautifulSoup


BASEURL = "https://letterboxd.com/"


def make_request(url):
    return requests.get(url)


def get_max_pages(username):
    response = make_request(f"{BASEURL}{username}/watchlist/")
    soup = BeautifulSoup(response.text, "html.parser")
    pagination = soup.find("div", class_="pagination").find_all("li")
    max_pages = int(pagination[-1].find("a").text)

    return max_pages


class LetterBoxd:
    @staticmethod
    def get_watchlist(usernames=["daniel_alba", "malejaa"]):
        result_global = []
        for username in usernames:
            print("username")
            result = []
            page = 1
            max_pages = get_max_pages(username)

            while page <= max_pages:
                response = make_request(f"{BASEURL}{username}/watchlist/page/{page}")

                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, "html.parser")

                    ul_element = soup.find("ul", class_="poster-list")

                    if ul_element:
                        images = ul_element.find_all("img", class_="image")

                        for image in images:
                            result.append(image.get("alt"))

                    page += 1

            result_global.append(result)

        set1 = set(result_global[0])
        set2 = set(result_global[1])

        coincidences = set1.intersection(set2)

        return "\n".join(coincidences)
