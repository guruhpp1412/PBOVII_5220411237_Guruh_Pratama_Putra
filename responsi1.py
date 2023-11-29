#Nama: Guruh Pratama Putra
#NIM :5220411237

class Karyawan:
    def __init__(self, nama, jabatan, tarif):
        self.nama = nama
        self.jabatan = jabatan
        self.tarif = tarif

    def calculate_salary(self, jam_kerja):
        hitung = self.tarif * jam_kerja
        return hitung

class FullTime(Karyawan):
    def __init__(self, nama, jabatan, tarif):
        super().__init__(nama, jabatan, tarif)
    
    def calculate_salary(self, jam_kerja):
        hitung = self.tarif * jam_kerja
        return hitung

class PartTime(Karyawan):
    def __init__(self, nama, jabatan, tarif):
        super().__init__(nama, jabatan, tarif)

    def calculate_salary(self, jam_kerja, lembur=None):
        if lembur != None:    
            return ((self.tarif * jam_kerja) + (10000*lembur))
        else:
            return (self.tarif * jam_kerja)
    
def menu():
    print('='*45)
    print('Gaji Karyawan')
    print('='*45)
    print('Jenis Karyawan: ')
    print('1. Full Time')
    print('2. Part Time')
    print('='*45)

def main():
    menu()
    pilih = int(input('1/2: '))

    if pilih == 1:
        nama = input("Nama :")
        jabatan = input('Jabatan :')
        tarif = 600000
        jam_kerja = 1
        k1 = FullTime(nama, jabatan, tarif)
        gaji1 = k1.calculate_salary(jam_kerja)
        print("Gaji kamu bulan ini adalah Rp", gaji1)
    elif pilih == 2:
        nama = input("Nama :")
        jabatan = input('Jabatan :')
        tarif = 15000
        jam_kerja = int(input('Jam Kerja :'))
        k2 = PartTime(nama, jabatan, tarif)
        print("Apakah kamu mengambil lembur? y/t")
        lem= str(input())
        if lem == 'y' or lem == 'Y':
            lembur=int(input('Berapa Lama Kamu Lembur (per Jam): '))
            hiL = k2.calculate_salary(jam_kerja, lembur)
            print("Gaji kamu bulan ini ditambah lembur yang diambil adalah Rp", hiL)
        else:
            hiN = k2.calculate_salary(jam_kerja)
            print("Gaji kamu bulan ini adalah Rp", hiN)
    else:
        print('Pilihan Tidak Ada!')

main()


        



