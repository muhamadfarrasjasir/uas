from model import daftar_nilai
from view import view_nilai

data = {'nama' : [], 'nilai' : []}

while True:
    print("[(l)ihat, (T)ambah, (U)bah, (C)ari, (H)apus, (K)eluar]")
    tanya = input("Masukkan Pilihan : ")
    match tanya:
        case "l":
            view_nilai.cetak_daftar_nilai(data)
            
        case "t":
            data = daftar_nilai.tambah_data(data)
            
        case "u":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("Masukkan Nama siswa yang akan diubah : ")
                data = daftar_nilai.ubah_data(data, nama)
        
        case "c":
            if len(data['nama']) > 0:
                # view_nilai.cetak_daftar_nilai(data)
                nama = input("masukkan nama yang akan dicari : ")
                data = daftar_nilai.cari_data(data, nama)
        
        case "h":
            view_nilai.cetak_daftar_nilai(data)
            if len(data['nama']) > 0:
                nama = input("masukkan nama yang akan dihapus : ")
                data = daftar_nilai.hapus_data(data, nama)
        
        case "k":
            print("anda sudah keluar dari program")
            break
        
        case _:
            print("tidak sesuai pilihan, silahkan pilih kembali\n")
            continue