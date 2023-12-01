class adopsi:
    def __init__(self, nama, umur, warna, harga):
        self.nama = nama
        self.umur = umur
        self.warna = warna
        self.harga = harga
    
    def ngeong(self):
        print('Miiaaawwwww........')

    def tampilkan(self):
        print("Nama: ", str(self.nama),", Umurnya: ",int(self.umur), "tahun, Warnanya: ", str(self.warna), ", Harganya: Rp", int(self.harga))

object1 = adopsi("Kitty", 2, "kuning", 50000)
object2 = adopsi("Kitten", 1, "hitam", 100000)

print("Nama Kucing 1: ", object1.nama)
print("Umur Kucing 1: ", object1.umur)
print("Warna Kucing 1: ", object1.warna)
print("Harga Kucing 1: ", object1.harga)
object1.ngeong()
object1.tampilkan()

print("\nNama Kucing 2: ", object2.nama)
print("Umur Kucing 2: ", object2.umur)
print("Warna Kucing 2: ", object2.warna)
print("Harga Kucing 2: ", object2.harga)
object2.ngeong()
object2.tampilkan()