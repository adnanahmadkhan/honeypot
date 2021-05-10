import pysftp
from utils.logger import LOG
from utils.util import get_filename_from_cd
from os.path import join, dirname
import requests



# Global variables for interacting with filesystems
dirname = dirname(__file__)
downloads_folder = join(dirname, 'downloads')



def extract_sftp(host, username, password, remote_path, remote_file):
    """
    Function for extracting file from SFTP server
    It saves file in downloads folder
    """
    try:        
        # TODO: Add hostkeys here, else file transfer not secure
        # cnopts = pysftp.CnOpts()
        # cnopts.hostkeys = None   

        with pysftp.Connection(host=host, username=username, password=password) as sftp:
            LOG.info(f"Connection succesfully established")

            # Switch to a remote directory
            sftp.cwd(remote_path)
            LOG.info(f"Changing directory on server successful::")

            LOG.info(f"Current file being Downloaded: {remote_file}")
            saveTo = join(downloads_folder, f'./{remote_file}')
            sftp.get(remote_file, saveTo)
    
    except Exception as e:
        LOG.error("SFTP Connection Exception::", exc_info=True)
    finally:
        sftp.close()



def extract_html(file_uri):
    """
    extracts csv/mp3 etc files from HTML URIs
    It saves file in downloads folder
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
    