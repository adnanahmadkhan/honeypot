import sqlite3
from utils import util

def load_into_table(data, table_name):
    """
    Load data into table of desired name
    """
    con = util.get_connection("datawarehouse.db")

    export = []

    cnt = 0
    for i in data:
        cnt+=1

        export.append((i["source_id"], i["data"]["name"], i["data"]["category"], i["data"]["length"], i["data"]["created_at"], i["scaled_legnth"],))

        # adding data in bulks
        if(cnt%100==0): 
            con.executemany("insert into person(source_id, name, category, length, scaled_length, created_at) values (?,?,?,?,?,?)", export)
            export = []
        
            
