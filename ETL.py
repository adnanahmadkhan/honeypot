from utils.logger import LOG
import extract
import json
from os.path import join, dirname

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

    filename = extract.extract_html(env["file_uri"])
    with open(join(downloads_folder, filename)) as json_file:
        data = json.load(json_file)

    print(dict(list(data.items())[:3]))

    
    
