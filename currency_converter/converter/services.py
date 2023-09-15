import requests
from bs4 import BeautifulSoup


def calc_rate(from_currency, to_currency, value) -> float:
    """ Парсинг валют с открытых источников. """
    
    URL = f"https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+{from_currency}+{to_currency}&sca_esv=565412338&sxsrf=AM9HkKnErIrFBqPBp8y5YgHaTHONIGUR9A%3A1694723603968&ei=E24DZeraOt-RwPAPua-TmAI&ved=0ahUKEwiqsKCz-aqBAxXfCBAIHbnXBCMQ4dUDCBA&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+EUR+RUB&gs_lp=Egxnd3Mtd2l6LXNlcnAiENC60YPRgNGBIEVVUiBSVUIyChAAGIAEGEYYggIyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCBAAGBYYHhgKMgYQABgWGB4yBhAAGBYYHkiVmwFQ8Q1YwpcBcAd4AZABAJgBqwGgAYINqgEEMTguMrgBA8gBAPgBAcICChAAGEcY1gQYsAPCAgoQABiKBRiwAxhDwgIHECMYigUYJ8ICEBAAGIAEGBQYhwIYsQMYgwHCAgsQABiABBixAxiDAcICCBAAGIAEGLEDwgIFEAAYgATCAg0QABiKBRixAxiDARhDwgIKEAAYgAQYFBiHAsICBxAAGIAEGArCAgsQLhiABBjHARivAcICDRAAGIAEGLEDGIMBGArCAg0QABiABBgUGIcCGLEDwgILEAAYFhgeGPEEGAriAwQYACBBiAYBkAYK&sclient=gws-wiz-serp"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

    full_page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(full_page.content, 'html.parser')

    convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

    rate = float(convert[0].text.replace(",", "."))
    try:
        value = float(value)
    except:
        ValueError("Неправильно введенна сумма для перевода")
    
    result_num: float = value * rate
    return round(result_num, 2)


if __name__ == '__main__':
    print(calc_rate("USD", "RUB", 100.1))