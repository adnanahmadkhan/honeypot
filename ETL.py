from utils.logger import LOG
import extract
import transform
import load
import json
from os.path import join, dirname
from utils import util
from math import isnan
import csv

# Global variables for interacting with filesystems
dirname = dirname(__file__)
downloads_folder = join(dirname, 'downloads')

# fetch environment
with open(join(dirname, '.env')) as f:
    env = json.load(f)


if __name__ == "__main__":
    """
    Main function to be run
    """

    # extract file from remote source
    # filename = extract.extract_html(env["file_uri"])
    filename = "codechallenge_data.json"
    
    # convert to dictionary
    with open(join(downloads_folder, filename)) as json_file:
        data = json.load(json_file)

    # apply transformation pipeline
    data = transform.convert_to_floats(data, "data,length")
    data = transform.remove_nans(data, "data,length")
    data = transform.remove_zeros(data, "data,length")
    data = transform.remove_empty_strings(data, "data,length")
    data = transform.remove_empty_strings(data, "data,category")
    data = transform.apply_scale_by_category(data)

    # load data to SQLite databases
    load.load_into_table(data)

    

    
    
    
