class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self._arvo = arvo
        self.edellinen = 0

    def miinus(self, operandi):
        self._arvo = self._arvo - operandi

    def plus(self, operandi):
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self.edellinen = self.arvo
        self._arvo = arvo

    def arvo(self):
        return self._arvo

    def kumoa(self):
        self.arvo = self.edellinen