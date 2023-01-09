from tabulate import tabulate

def cetak_daftar_nilai(data):
    i = range(1, len(data['nama'])+1)
    
    headers = ["No", "Nama", "Nilai"]
    if len (data['nama']) > 0:
        print(tabulate(data, headers, showindex=i,tablefmt="rounded_outline"))
    
    else:
        print("\n tidak ada data")

def cetak_hasil_pencarian(dataMhs):
    print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))