import os
import requests
from tqdm import tqdm

BASE_DIR = os.path.abspath(os.path.dirname(__name__))


def download_model(model_name=""):
    subdir = os.path.join(BASE_DIR, 'application\\models', model_name)
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    subdir = subdir.replace('\\', '/')  # needed for Windows
    download_name = 'models/117M'
    for filename in ['checkpoint', 'encoder.json', 'hparams.json', 'model.ckpt.data-00000-of-00001', 'model.ckpt.index',
                     'model.ckpt.meta', 'vocab.bpe']:

        r = requests.get("https://storage.googleapis.com/gpt-2/" + download_name + "/" + filename, stream=True)

        with open(os.path.join(subdir, filename), 'wb') as f:
            file_size = int(r.headers["content-length"])
            chunk_size = 1000
            with tqdm(ncols=100, desc="Fetching " + filename, total=file_size, unit_scale=True) as pbar:
                # 1k for chunk_size, since Ethernet packet size is around 1500 bytes
                for chunk in r.iter_content(chunk_size=chunk_size):
                    f.write(chunk)
                    pbar.update(chunk_size)
    return "Model Downloaded Successfully"
