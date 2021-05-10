import pysftp
from utils.logger import LOG
from utils.util import get_filename_from_cd
from os.path import join, dirname
import requests
import pandas as pd



# Global variables for interacting with filesystems
dirname = dirname(__file__)
downloads_folder = join(dirname, 'downloads')


def extract_html(file_uri):
    """
    Extracts csv/json etc files from HTML URIs
    It saves file in downloads folder
    Returns the name of the file
    """
    r = requests.get(file_uri, allow_redirects=True)
    filename = get_filename_from_cd(r.headers.get('content-disposition'))
    if (not filename):
        if file_uri.find('/'):
            filename = file_uri.rsplit('/', 1)[1]
        else:
            filename = "filename"
    saveTo = join(downloads_folder, f'./{filename}')
    open(saveTo, 'wb').write(r.content)

    return filename


def df_from_json(filepath):
    """
    Gets data from JSON file and returns a pandas dataframe
    """
    return pd.read_json(filepath)



    