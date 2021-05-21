import urllib
import zipfile

def download_and_unzip(map):
    url = "https://movingai.com/benchmarks/street/" + map + ".zip"
    extract_dir = "maps"

    zip_path, _ = urllib.request.urlretrieve(url)
    with zipfile.ZipFile(zip_path, "r") as f:
        f.extractall(extract_dir)