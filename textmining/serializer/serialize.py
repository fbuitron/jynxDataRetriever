""" Serializer is the module in charge of writting objects to files and retrieve them"""

import pickle
from pathlib import Path


def dump_object(obj, file_path, file_name):
    """Serializes object to the file_path/file_name"""

    final_file_name = get_file_name(file_path, file_name)
    target_file = open(final_file_name, "wb")
    pickle.dump(obj, target_file)
    target_file.close()



def get_object(file_path, file_name):
    """Reads an object from the file system"""

    target_file_name = get_file_name(file_path, file_name)
    target_file = Path(target_file_name)

    if target_file.is_file():
        return pickle.load(open(target_file_name, "rb"))
    else:
        raise Exception("File not found ", target_file_name)

def get_file_name(file_path, file_name):
    """Returns the final path given the path and name"""

    return "%s%s" % (file_path, file_name)
