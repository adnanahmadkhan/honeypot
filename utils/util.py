import re
# helper function
def get_filename_from_cd(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall(f'filename\*?=["]?(?:UTF-\d["]*)?([^;\r\n"]*)["]?;?', cd)
    if len(fname) == 0:
        return None
    return fname[0]