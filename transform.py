import pandas as pd
import re
from utils import util


def convert_to_floats(data, key):
    """
    Generic function that
    Converts nested dictionary values into complete float
    from strings that are not empty.

    returns back data if exception occurs
    returns transformed list if all goes well
    """

    try:
        key.replace(" ", "")
        keys = key.split(",")
        results = []

        for i in data:
            val = i[keys[0]][keys[1]]
            if(val != "" and isinstance(val, str)):
                    i[keys[0]][keys[1]] = float(re.findall("\d+\.\d+", val)[0])
            results.append(i)

    except Exception as e:
        print(f"An Exception occurred:: {e}")
        return data

    print(len(results))
    return results




def remove_nans(data, key):
    """
    Removes nan from nested dict
    """
    key.replace(" ", "")
    keys = key.split(",")

    results = []
    for my_dict in data:
        if not pd.isna(my_dict[keys[0]][keys[1]]):
            results.append(my_dict)
    print(len(results))
    return results




def remove_empty_strings(data, key):
    """
    Removes nan from nested dict
    """
    key.replace(" ", "")
    keys = key.split(",")

    results = []
    for my_dict in data:
        if my_dict[keys[0]][keys[1]] != "":
            results.append(my_dict)
    print(len(results))
    return results


def remove_zeros(data, key):
    """
    Removes zeros from int/float values
    """
    key.replace(" ", "")
    keys = key.split(",")

    results = []
    for my_dict in data:
        val = my_dict[keys[0]][keys[1]]

        if not isinstance(val, str) and my_dict[keys[0]][keys[1]] != 0:
            results.append(my_dict)
    print(len(results))
    return results


def apply_scale_by_category(data):
    """ Transforms the legnth parameter using
    category
    :param conn: the Connection object
    :param category
    :return: the scale
    """
    con = util.get_connection("datawarehouse.db")
    
    results = []
    for i in data:
        cat = i["data"]["category"]
        scale = float(util.get_scale_by_category(con, cat)[0])
        i["scaled_legnth"] = scale * i["data"]["value"]
    return row


