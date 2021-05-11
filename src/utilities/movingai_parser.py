import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_map_list():
    url = 'https://movingai.com/benchmarks/street/index.html'
    requests.get(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    table_data = soup.find('table')

    headers = []
    for i in table_data.find_all('tr')[0]:
        title = i.text
        headers.append(title)

    df = pd.DataFrame(columns=headers)

    for j in table_data.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [tr.text for tr in row_data]
        length = len(df)
        df.loc[length] = row

    return df


def download_zip(url, chunk_size=128):
    r = requests.get(url, stream=True)
    save_path = "temp/"
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
