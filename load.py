import sqlite3
from utils import util

def load_into_table(data, table_name):
    """
    Load data into table of desired name
    """

    try:
        con = util.get_connection("datawarehouse.db")
        con.execute("create table features (source_id, name, category, length, scaled_length, created_at)")

        export = []

        cnt = 0
        for i in data:
            cnt+=1

            export.append((i["source_id"], i["data"]["name"], i["data"]["category"], i["data"]["length"], i["data"]["created_at"], i["scaled_legnth"],))

            # adding data in bulks
            if(cnt%100==0): 
                print(export)
                con.executemany("insert into features(source_id, name, category, length, scaled_length, created_at) values (?,?,?,?,?,?)", export)
                export = []
            
    except:
        print("Exception occured")
    finally:
        con.close()
