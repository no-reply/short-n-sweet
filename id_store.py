from os import makedirs
from os.path import isdir, join, realpath, isfile
import dbm.gnu

FILENAME=".identifier_store"

class IdStore:

    def __init__(self, target, mode=0):
        if isfile(join(target, FILENAME)):
            if mode > 0:
                self.db = dbm.gnu.open(FILENAME, 'ws')
            else:
                self.db = dbm.gnu.open(FILENAME, 'ru')
        elif mode == 2:
            self.db = dbm.gnu.open(FILENAME, 'c')

    #
    # Write Methods
    #

    def addId(self, identifier, url, metadata=None):
        if isinstance(identifier, str) and isinstance(url, str):
            self.db[identifier] = url
            self.addMetadata(identifier, metadata)

    def deleteId(self, identifier):
        del self.db[identifier]
        

    #
    # Read Methods
    #

    def getId(self, identifier):
        try:
            return str(self.db[identifier], 'utf-8')
        except KeyError:
            return None
