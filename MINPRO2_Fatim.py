import pwinput
from prettytable import PrettyTable

print("Sistem Pengajuan Cuti Karyawan PT. FJ")

akun = {
    "admin": {
        "nama": "admin",
        "password": "admin123",
        "role": "admin"
    },
    "fatim": {
        "nama": "fatim",
        "password": "fatim123",
        "role": "user"
    },
    "timah": {
        "nama": "timah",
        "password": "timah123",
        "role": "user"
    }
}

daftar_cuti = []

def input_wajib(pesan):
    data = input(pesan)
    while data.strip() == "":
        print("Input tidak boleh kosong.")
        data = input(pesan)

    return data.strip()

def input_angka(pesan):
    data_angka = input(pesan)
    while not data_angka.isdigit() or int(data_angka) <= 0:
        print("Input harus berupa angka lebih dari 0.")
        data_angka = input(pesan)
    return int(data_angka)

def login():
    while True:
        print("Halaman Login")
        username = input("Username: ")
        password = pwinput.pwinput(
            prompt= "Password: ", mask="*"
            )
        if username in akun:
            if password == akun[username]["password"]:
                print("Login berhasil!")
                print("Selamat datang,", akun[username]["nama"])
                print("Role: ", akun[username]["role"])
                return username
            else:
                print("Password salah.")
        else:
            print("Username tidak ditemukan.")

def status_cuti(jumlah_hari):
    if jumlah_hari <= 5:
        return "Diterima"
    else:
        return "Ditolak"

def tabel(data):
    if len(data) == 0:
        print("Tidak ada data cuti.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID Cuti", "Nama", "Jumlah Hari Cuti", "Alasan", "Status"]
    for cuti in data:
        tabel.add_row([cuti["ID Cuti"], cuti["Nama"], cuti["Jumlah Hari Cuti"], cuti["Alasan"], cuti["Status"]])
    print(tabel)

def cari_cuti(id_cuti):
    for cuti in daftar_cuti:
        if cuti["ID Cuti"] == id_cuti:
            return cuti
    return None

def ajukan_cuti(username):
    id_cuti = input_wajib("ID Cuti: ")
    while cari_cuti(id_cuti) is not None:
        print("ID Cuti sudah digunakan.")
        id_cuti = input_wajib("Masukkan ID Cuti yang lain: ")

    if akun[username]["role"] == "admin":
        pemilik = input_wajib("Masukkan username pemilik cuti: ")
        while pemilik not in akun or akun[pemilik]["role"] != "user":
            print("Username karyawan tidak ditemukan.")
            pemilik = input_wajib("Masukkan username pemilik cuti: ")
    else:
        pemilik = username
    
    nama = input_wajib("Masukkan Nama: ")
    jumlah_hari = input_angka("Jumlah hari cuti: ")
    alasan = input_wajib("Alasan cuti: ")
    status = status_cuti(jumlah_hari)
    data = {
        "ID Cuti": id_cuti,
        "Nama": nama,
        "Jumlah Hari Cuti": jumlah_hari,
        "Alasan": alasan,
        "Status": status
        }
    daftar_cuti.append(data)
    print("Pengajuan cuti berhasil ditambahkan.")
    print("Status cuti:", status)

def lihat_riwayat(username):
    data_riwayat = []
    if akun[username]["role"] == "admin":
        tabel(daftar_cuti)
    else:
        data_sendiri = []
        for cuti in daftar_cuti:
            if cuti["Nama"] == akun[username]["nama"]:
                data_sendiri.append(cuti)
                tabel(data_sendiri)

def ubah_cuti(username):
    id_cuti = input_wajib("Masukkan ID Cuti yang ingin diubah: ")
    cuti = cari_cuti(id_cuti)
    if cuti is None:
        print("ID Cuti tidak ditemukan.")
        return

    if akun[username]["role"] == "user":
        if cuti["pemilik"] != username:
            print("Anda tidak bisa mengubah cuti selain milik anda.")
            return

    print("1. Ubah Nama")
    print("2. Ubah Jumlah Hari Cuti")
    print("3. Ubah Alasan")
    pilihan_ubah = input("Pilih data yang ingin diubah (1-3): ")
    if pilihan_ubah == "1":
        nama_baru = input_wajib("Masukkan nama baru: ")
        cuti["Nama"] = nama_baru
    elif pilihan_ubah == "2":
        jumlah_hari_baru = input_angka("Masukkan jumlah hari cuti baru: ")
        cuti["Jumlah Hari Cuti"] = jumlah_hari_baru
        cuti["status"] = status_cuti(jumlah_hari_baru)
    elif pilihan_ubah == "3":
        alasan_baru = input_wajib("Masukkan alasan baru: ")
        cuti["Alasan"] = alasan_baru
    else:
        print("Pilihan tidak valid.")
        return
    print("Data cuti berhasil diubah.")

def batalkan_cuti(username):
    id_cuti = input_wajib("Masukkan ID Cuti: ")
    cuti = cari_cuti(id_cuti)

    if cuti is None:
        print("ID Cuti tidak ditemukan.")
        return

    if akun[username]["role"] == "user":
        if cuti["pemilik"] != username:
            print("Anda tidak bisa mengubah cuti selain milik anda.")
            return

    daftar_cuti.remove(cuti)
    print("Pengajuan cuti berhasil dibatalkan.")

username = login()
role = akun[username]["role"]

while True:
    print("MENU UTAMA")
    print("1. Ajukan Cuti")
    print("2. Lihat Riwayat Cuti")
    print("3. Ubah Pengajuan Cuti")
    print("4. Batalkan Pengajuan Cuti")
    print("5. LOGOUT")

    pilihan = input("Pilih menu (1-5): ")
    if pilihan == "1":
        ajukan_cuti(username)
    elif pilihan == "2":
        lihat_riwayat(username)
    elif pilihan == "3":
        ubah_cuti(username)
    elif pilihan == "4":
        batalkan_cuti(username)
    elif pilihan == "5":
        print("Anda berhasil logout.")
        break
    else:
        print("Pilihan tidak ditemukan.")

        


