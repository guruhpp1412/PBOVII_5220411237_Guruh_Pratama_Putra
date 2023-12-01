def variabel():
    print("="*35)
    print("                NAMA VARIABEL               ")
    print('============================================')
    nama=str(input('1. Nama: ' ))
    umur=int(input('2. Umur: '))
    jenis=str(input('3. Jenis: '))
    harga=str(input('4. Harga: '))

def info():
    print("===========================================================")
    print("INFO")
    print("Penghasilan > Rp 10.000.000, jumlah diambil 3")
    print("Penghasilan Rp 5.000,000 - Rp 10.000.000, jumlah diambil 2")
    print("Penghasilan Rp 1.000.000 - Rp 5.000.000, jumlah diambil 3")
    print(" KALAU ADA KECURANGAN ANDA DIBAN")
    print("===========================================================")

def penghasilan():
    penghasilan=int(input('Penghasilan: '))
    return penghasilan

def jumlah():
    jumlah=int(input('Jumlah yang dapat diambil: '))
    return jumlah

def kondisi():
    i=0
    b=jumlah()
    while i < b:
        variabel()
        i+=1
        
def sistem():
    info()
    a= penghasilan()
    if a > 10000000: 
        kondisi()
        print("Selesai")
    elif 5000000 <= a <= 10000000:
        kondisi()
        print("selesai")
    elif 1000000 <= a <= 5000000:
        kondisi()
        print("selesai")
    else:
        print("Tidak Memadai")

sistem()