class Club:
    def __init__(self, nama, pemain):
        self.nama = nama
        self._pem = pemain

    def tampil(self):
        print("Klub", self.nama, "Nama Pemain", self._pem)

    #overloding
    def tampilNo(self, nomor=None):
        if nomor != None :
            pungg = nomor
            print("Klub", self.nama, "Nama Pemain", self._pem, "No.", pungg)
        else:
            print("Klub", self.nama, "Nama Pemain", self._pem,". Bukan Pemain Kami !")

class Pelatih(Club):
    def __init__(self, nama, pemain, coach):
        super().__init__(nama, pemain)
        self.coach = coach

    #overriding
    def tampil(self):
        print("Klub", self.nama, "Nama Pemain", self._pem, "Pelatih", self.coach)

    def tampilNo(self, nomor=None):
        return super().tampilNo(nomor)

pemain1=Club("Manchester United", "Maguire")
pemain1.tampil()
pemain1.tampilNo()
print("="*50)
pemain2=Pelatih("Manchester United", "Fernandes", "Ten Hag")
pemain2.tampil()
pemain2.tampilNo(8)