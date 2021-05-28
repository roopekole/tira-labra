import urllib
import zipfile

def process_map(map):
    download_and_unzip(map)
    path = "maps/" + map
    with open(path, "r") as map_file:
        # Unnecessary metadata on first four rows will be omitted
        data = map_file.read()
    return make_nested_list(data)

def download_and_unzip(map):
    url = "https://movingai.com/benchmarks/street/" + map + ".zip"
    extract_dir = "maps"

    zip_path, _ = urllib.request.urlretrieve(url)
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(extract_dir)


def make_nested_list(str, delim='\n'):
    return [list(e) for e in str.split(delim)]