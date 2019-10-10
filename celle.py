class Celle:
    def __init__(self):
        self._status = False

    def settDoed(self):
        self._status = False

    def settLevende(self):
        self._status = True
	
    def erLevende(self):
        return self._status
	
    def hentStatusTegn(self):
        if self._status:
            return "O"
        else:
            return "."