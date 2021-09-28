# Write generator that yields all files in directory matching specified pattern.
# Note: Function should handle all subdirectories in the directory
import os
import re


def get_files(entry_path, pattern):
    """
    Yields all files in given directory (recursively)
    :param entry_path: directory name
    :param pattern: specifies name of the file
    """

    for root, dirnames, filenames in os.walk(entry_path, topdown=True):
        try:
            for file in filenames:
                if re.search(f'{pattern}', file) and os.path.isfile(os.path.join(root, file)):
                    yield os.path.join(root, file)
        except re.error as err:
            print(f'Invalid Pattern - {err}')
            raise SystemExit
