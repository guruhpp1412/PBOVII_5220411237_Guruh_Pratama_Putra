class mataKuliah:
    def __init__(self, mk, sks, nilai):
        self.mk = mk
        self.sks = sks
        self.nilai = nilai

class IPK:
    def __init__(self):
        self.jumlah_matkul = []

    def tambah_matkul(self, mk, sks, nilai):
        matkul = mataKuliah(mk, sks, nilai)
        self.jumlah_matkul.append(matkul)

    def konversi_nilai(self, nilai):
        konversi = {'A': 4, 'B': 3,'C': 2, 'D': 1, 'E': 0}
        return konversi.get(nilai, 0)

    def hitung_ipk(self):
        total_sks = 0
        total_nilai = 0

        for matkul in self.jumlah_matkul:
            total_sks += matkul.sks
            total_nilai += matkul.sks * self.konversi_nilai(matkul.nilai)

        if total_sks == 0:
            return 0.0
        else:
            ipk = total_nilai / total_sks
            return ipk

def hitung_ipk():
    penghitung = IPK()

    while True:
        print('='*30)
        print("Menu:")
        print("1. Tambah Mata Kuliah")
        print("2. Hitung IPK")
        print("3. Keluar")
        print('='*30)

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            mk = str(input("\nNama Mata Kuliah: "))
            sks = int(input("Bobot Kredit (sks): "))
            nilai = str(input("Nilai (A, B, C, D, E): ")).upper()
            penghitung.tambah_matkul(mk, sks, nilai)
        elif pilihan == '2':
            ipk = penghitung.hitung_ipk()
            print(f"IPK Anda adalah: {ipk:.2f}")
            break
        elif pilihan == '3':
            break
        else:
            print("Pilihan Tidak Ada!!!")


if __name__ == "__main__":
    hitung_ipk()
