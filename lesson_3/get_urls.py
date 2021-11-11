import requests


def get_urls():
    try:
        my_file = open("urls.txt", "r")
        results = ""
        for url in my_file.readlines():
            res = requests.get(url.strip())
            if res.status_code == 200:
                results += f"{url.strip()}: {res.status_code}\n"
        my_file.close()
        print(results, end='')
    except BaseException as e:
        print("error_xxxxx", str(e.args))


get_urls()
