class Club:
    def __init__(self, var1, var2, var3):
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3
    
    def displayPublic(self):
        print("Club: ", self.var1)

    def _displayProtected(self):
        print("Club: ", self._var2)

    def __displayPrivate(self):
        print("Club: ", self.__var3)

    def accessPrivate(self):
        self.__displayPrivate()

class Pemain(Club):
    def __init__(self, var1, var2, var3, nama):
        super().__init__(var1, var2, var3)
        self.nama = nama

    def displayPemain(self):
        print("Nama: ", self.nama)

#club_bola= Club("MU", "ManCity", "Liverpool")
nama_pemain= Pemain("Arsenal", "Totenham", "Burnley", "Ronaldo")

#print(club_bola.displayPublic())
#print(club_bola._displayProtected())
#print(club_bola.accessPrivate())
print(nama_pemain.displayPublic())
print(nama_pemain._displayProtected())
print(nama_pemain.accessPrivate())
print(nama_pemain.displayPemain())