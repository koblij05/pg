import sys
import requests


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    try:
        r = requests.get(url)
    except Exception as e:
        print("Nastala chyba při stahování obsahu.")
        print(e)
        return None       
    if r.status_code != 200:
        print(f"Stahovani skoncilo chybou: {r.status_code}")
        return None
    hrefs = []
    a_start = 0
    while a_start != -1:
        a_start = r.text.find("<a ", a_start)
        if a_start != -1:
            a_end = r.text.find("</a>", a_start)
            if a_end != -1:
                a = r.text[a_start:a_end + len("</a>")]
                #print(a)
                href_start = a.find('href="')
                if href_start != -1:
                    href_end = a.find('"', href_start + 6)
                    if href_end != -1:
                        href = a[href_start+6:href_end]
                        #print(href)
                        if href not in hrefs:
                            hrefs.append(href)
                    else:
                        print("HTML má syntaktické chyby!")
                a_start = a_end + 1
            else:
                print("HTML má syntaktické chyby! Ukončuju hledání.")
                sys.exit(1)
    hrefs
    return hrefs


if __name__ == "__main__":
    try:
        if len(sys.argv) <= 1:
            print("Není zadán žádný URL. Je nutné použít parametr při spuštění.")
            sys.exit(1)
        url = sys.argv[1]
        hrefs = download_url_and_get_all_hrefs(url)
        if hrefs != None:
            for href in hrefs:
                print(href)
            print(f"Nalezeno {len(hrefs)} odkazů.")
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
