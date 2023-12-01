class PerpusItem:
    def __init__(self, judul, subjek):
        self.judul=judul
        self.subjek=subjek

    def LokasiPenyimpanan(self):
        print('Nama Judul',self.judul,'. Subjeknya',self.subjek)

    def info(self):
        print('Judul',self.judul,'Itu ada!')

class Buku(PerpusItem):
    def __init__(self, judul, subjek, ISBN, pengarang, jmlHal, ukuran):
        super().__init__(judul, subjek)
        self.ISBN = ISBN
        self.pengarang = pengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran
    
    def tampilBuku(self):
        print('ISBN',self.ISBN,',Judul',self.judul,',Pengarang',self.pengarang,'Jumlah Halaman dan ukuran',self.jmlHal,'&',self.ukuran, 'cm')

class Majalah(PerpusItem):
    def __init__(self, judul, subjek, volume, issue):
        super().__init__(judul, subjek)
        self.volume = volume
        self.issue = issue

    def tampilMajalah(self):
        print('Judul', self.judul, '. Volume dan Issue', self.volume, '&', self.issue)

class DVD(PerpusItem):
    def __init__(self, judul, subjek, aktor, genre):
        super().__init__(judul, subjek)
        self.aktor = aktor
        self.genre = genre

    def tampilDVD(self):
        print('Judul', self.judul, '. Aktor', self.aktor,', Genre', self.genre)

class Pengarang :
    def __init__(self, nama):
        self.nama = nama

    def infoPengarang(self):
        print ('Pengarang dari buku ini adalah', self.nama)
    
    def cariPengarang(self):
        print(self.nama, 'Pengarang Ditemukan !!')

class Katalog:
    def __init__(self, cari):
        self.search = cari

    def cari(self):
        print('Info,',self.search)

orang1 = PerpusItem('Malin Kundang','Dongeng')
orang1.LokasiPenyimpanan()
orang1.info()
print('='*55)
orang2 = Buku('Malin Kundang', 'Dongeng', 122, 'M.Rinaldi', 33,50)
orang2.tampilBuku()
print('='*55)
oar = Katalog('tidak ada di Perpus Item')
oar.cari()
print('='*55)
pengarang = Pengarang('M.Rayai',)
orang3 = Buku('Bulan', 'Fiksi', 33, pengarang, 23, 35)
print('Nama Pengarang:', orang3.pengarang)
