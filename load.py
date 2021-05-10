import sqlite3
from utils import util

def load_into_table(data):
    """
    Load data into table of desired name
    """

    try:
        con = util.get_connection("datawarehouse.db")
        con.execute("drop table if exists features")
        con.execute("create table features (source_id, name, category, length, scaled_length, created_at)")

        export = []
        sql = """insert into features (source_id, name, category, length, scaled_length, created_at) values (?,?,?,?,?,?)"""
        cnt = 0
        for i in data:
            cnt+=1
            tmp = (i["source_id"], i["data"]["name"], i["data"]["category"], i["data"]["length"], i["scaled_legnth"], i["data"]["created_at"])
            con.execute(sql, tmp)
            export.append(tmp)
            # adding data in bulks
            if(cnt%500000==0): 
                con.executemany(sql, export)
                export = []
            # adding last bulk
            con.executemany(sql, export)
    except Exception as e:
        print(f"Exception occured :: {e}")
    finally:
        con.close()
