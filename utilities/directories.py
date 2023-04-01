import main_directory
import os

class Directories:
    def __init__(self):
        self._main_directory = main_directory.dir_path
        self._database_directory = os.path.join(self._main_directory, 'utilities', 'database')

    def get_main_directory(self):
        return self._main_directory

    def get_database_directory(self):
        return self._database_directory
