import re
import sqlite3


# helper functions

def get_filename_from_cd(cd):
    """ Get filename from content-disposition
    :param db_file: content disposition header
    :return: filename
    """
    if not cd:
        return None
    fname = re.findall(f'filename\*?=["]?(?:UTF-\d["]*)?([^;\r\n"]*)["]?;?', cd)
    if len(fname) == 0:
        return None
    return fname[0]




def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn



def get_scale_by_category(conn, category):
    """ Query scale by category
    :param conn: the Connection object
    :param category
    :return: the scale
    """
    
    cur = conn.cursor()
    cur.execute("SELECT scale_value FROM category_lookup WHERE category=?", (category,))

    row = cur.fetchone()
    return row