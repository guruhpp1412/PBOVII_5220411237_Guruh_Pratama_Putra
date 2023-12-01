class Menu:
    def __init__(self, rendang, sate, bakso):
        self.rendang = rendang
        self._sate = sate
        self.__bakso = bakso

a= Menu("Rendang", "Sate Madura", "Bakso Urat")

print(a.rendang)
print(a._sate)
print(a._Menu__bakso)