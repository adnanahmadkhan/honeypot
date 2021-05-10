from utils.logger import LOG
import extract
import json
from os.path import join, dirname
import pandas as pd

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
    # extract.extract_sftp(env["hostname"], env["username"], env["password"], env["remote_path"], env["remote_file"])
    extract.extract_html(env["file_uri"])