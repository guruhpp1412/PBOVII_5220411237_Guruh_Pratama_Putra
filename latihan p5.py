class Kamera:
    def __init__(self, jenis, tarif):
        self.jenis = jenis
        self._tarif = tarif

    def hitung_biaya_sewa(self, jumlah_hari):
        hitung=self._tarif * jumlah_hari
        return hitung

class DSLR(Kamera):
    def __init__(self):
        super().__init__("Kamera DSLR", 200000)

class Mirrorless(Kamera):
    def __init__(self):
        super().__init__("Mirrorless", 300000)

class ActionCam(Kamera):
    def __init__(self):
        super().__init__("Action Camera", 350000)

def menu():
    print("="*40)
    print("Selamat datang di Rental Kamera!")
    print("Jenis kamera dan tarif sewa per hari:")
    print("1. DSLR      : Rp 200.000/hari")
    print("2. Mirrorless: Rp 300.000/hari")
    print("3. Action Cam: Rp 350.000/hari")
    print("="*40)

def main():
    menu()
    pilihan = int(input("\nPilih jenis kamera: "))
    jumlah_hari = int(input("Masukkan sewa hari: "))

    if pilihan == 1:
        kamera = DSLR()
    elif pilihan == 2:
        kamera = Mirrorless()
    elif pilihan == 3:
        kamera = ActionCam()
    else:
        print("Pilihan tidak valid.")
        return

    biaya_sewa = kamera.hitung_biaya_sewa(jumlah_hari)
    print("\nBiaya sewa untuk", kamera.jenis, "selama", jumlah_hari, "hari adalah: Rp", biaya_sewa)

if __name__ == "__main__":
    main()
