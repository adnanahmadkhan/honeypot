import sqlite3
from utils import util

def load_into_table(data):
    """
    Load data into table of desired name
    """

    try:
        con = util.get_connection("datawarehouse.db")
        c = con.cursor()
        c.execute("drop table if exists features")
        c.execute("create table features (source_id, name, category, length, scaled_length, created_at)")

        export = []
        sql = """insert into features (source_id, name, category, length, scaled_length, created_at) values (?,?,?,?,?,?)"""
        cnt = 0
        for i in data:
            cnt+=1
            tmp = (str(i["source_id"]), str(i["data"]["name"]), str(i["data"]["category"]), str(i["data"]["length"]), str(i["scaled_legnth"]), str(i["data"]["created_at"]))
            export.append(tmp)

            # adding data in bulks
            if(cnt%500000==0): 
                print(export[:10])
                c.executemany(sql, export)
                export = []

            # adding last bulk
            print(export[:10])
            c.executemany(sql, export)
    except Exception as e:
        print(f"Exception occured :: {e}")
    finally:
        con.close()
