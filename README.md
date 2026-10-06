# MINPRO-2-DDP-PengajuanCuti
**MINI PROJECT 2 DASAR-DASAR PEMOGRAMAN**<br>
**NAMA: Fatimatu Jahra**<br>
**NIM: 2609116033**<br>
**KELAS: A**<br>
**TEMA: Sistem Pengajuan Cuti Karyawan**<br>

**1. Penjelasan Singkat Program**<br>
  Sebuah sistem sederhana dimana ada 2 role yaitu admin dan user, kedua role dapat menambah, melihat, mengubah, dan menghapus data, dengan catatan khusus role user tidak bisa melihat, mengubah, dan menghapus data selain miliknya sendiri. PT. FJ memiliki ketentuan jumlah hari cuti dimana jika jumlah hari cuti lebih daripada 5 hari maka status pengajuan akan otomatis ditolak.

**2. FLOWCHART**<br>
  a. Halaman Login<br>
  <img width="2524" height="4096" alt="FLOWCHART MINPRO 2-Login drawio" src="https://github.com/user-attachments/assets/ed78d4b1-662e-4798-bb02-21e7841978e2" /><br>
  Setelah program mulai, hal pertama yang dilakukan adalah inisialisasi akun dalam bentuk dictionary dan daftar_cuti dalam bentuk list untuk menyimpan data. Selanjutnya program akan menampilkan judul, lalu pengguna akan memasukkan username, apabila inputan tidak diisi maka data akan divalidasi dan menampilkan teks "input tidak boleh kosong", setelahnya pengguna akan diarahkan untuk input username kembali hingga benar. Setelah inputan telah terisi maka akan dilanjut dengan memasukkan password, sama seperti saat inputan username, pabila inputan kosoong maka program akan kembali ke masukkan username. Setelah terisi, program akan cek apakah username ada di dalam dictionary, jika tidak ada maka program akan menampilkan "username tidak ditemukann." dan kembali untuk input username. Setelah cek data username, selanjutnya dilakukan cek data password apakah sesuai dengan username yang ada di data akun atau tidak, jika tidak maka akan menampilkan "password salah." dan pengguna akan mengisi username kembali, jika ya maka program akan menampilkan login berhasil dan menampilkan menu. <br>

  b. Menu<br> 
  <img width="2448" height="4796" alt="FLOWCHART_MINPRO2_Menu drawio" src="https://github.com/user-attachments/assets/6ff6569c-e65a-4b56-bd66-70f4db2a1466" /> <br>
  Didalam tampilan menu, akan ditampilkan 5 menu dan pengguna akan diarahkan untuk menginput pilihan 1-5, jika pilihan kosong atau lebih daripada 5 maka program akan menampilkan "pilihan tidak tersedia" dan akan diarahkan ke tampilan menu lagi. Sesuai dengan pilihan, jika pengguna input 1 maka akan menampilkan program ajukan cuti, dst. <br>

  c. 1. Ajukan Cuti <br>
   <img width="2682" height="5280" alt="FLOWCHART MINPRO 2-1 drawio (3)" src="https://github.com/user-attachments/assets/aa845401-41d9-4cfc-9c3c-a21927673295" /> <br>
 <br>
  pada menu pilihan pertama yaitu ajukan cuti, pengguna akan diminta untuk menginput id cuti, jika inputan kosong atau id cuti sudah digunakan, maka pengguna akan diarahkan untuk mengisi id cuti kembali. Ketika id cuti sudah terisi dan belum digunakan, maka program akan memproses apakah role pengguna adalah admin atau bukan, jika admin maka pengguna akan menginput username pemilik cuti, jika inputan kosong maka akan diarahin untuk mengisi lagi, program cek apakah username yang diinput ada dalam data akun, jika tidak ada maka akan diarahkan untuk mengisi lagi. Begitu seterusnya hingga penentuan status cuti, program akan cek apakah jumlah hari cuti lebih kecil daripada samadengan 5, jika ya maka status cuti diterima, jika tidak maka status cuti diterima. Setelahnya pengguna akan diarahkan kembali ke menu. <br>

  d. 2. Lihat Riwayat Cuti <br>
  <img width="1600" height="1312" alt="FLOWCHART MINPRO 2-2 drawio" src="https://github.com/user-attachments/assets/9bac74b8-1f06-4112-9134-e81652934fea" /> <br>
  pada bagian lihat riwayat cuti, program akan identifikasi terlebih dahulu apakah pengguna memiliki role admin, jika ya maka akan menampilkan data riwayat yang berisi semua riwayat cuti, jika tidak maka akan menampilkan data sendiri. Setelahnya akan langsung diarahkan kembali ke menu. <br>

  e. 3. Ubah Riwayat Cuti <br>
  <img width="5019" height="3306" alt="FLOWCHART MINPRO 2-3 drawio (3)" src="https://github.com/user-attachments/assets/043fcdeb-9b32-4232-bb91-72012513bebc" /> <br>
  pada bagian ubah riwayat cuti, yang pertama muncul adlah pengguna menginput id cuti yang ingin diubah, kemudian program cek apakah id cuti ada dalam daftar cuti, jika tidak maka akan dikembalikan ke masukkan id cuti, jika ya maka program akan menidentifikasi username dan role, jika role bukan user maka akan diidentifikasi lagi apakah pemilik tidak sama dengan username, jika ya maka akan menampilkan anda tiak bisa mengubah cuti selain milik adn dan kembali ke masukkan id cuti. Jika pemilik sama dengan username maka program akan menampilkan 3 pilihan menu yang ingin diubah, kemudian pengguna akan menginput piliha, jika inputan kosong atau lebih dari 3 maka akan menampilkan pilihan tidak valid dan diarahkan kembali ke menu. Jika pilihan 1 maka akan diarahkan untuk menginput nama baru kemudian validasi input, setelahnya akan ditampilkan data cuti berhasil diubah dan kembali ke menu. Jika pilihan 2 maka pengguna akan memasukkan jumlah hari baru, jika inputan kosong atau angka berubah kurang dari 0 maka pengguna akan diarahkan untuk mengisi jumlah hari baru, setelahnya akan ditampilkan bahwa data cuti berhasil diubah dan diarahkan kembali ke menu. Jika pilihan 3 maka penggun akan memasukkan alasan baru kemudian validasi input dan akan ditampilkan data cuti berhqsil diubah lalu diarahkan kembali ke menu. <br>

  f. 4. Batalkan Pengajuan Cuti <br>
  <img width="2520" height="3952" alt="FLOWCHART MINPRO 2-4 drawio" src="https://github.com/user-attachments/assets/10e45aed-5d0a-4fa8-a952-a6ed51e82b9a" /> <br>
  pada bagian ini, pengguna akan menginput data id cuti yang ingin dihapus, kemudian dilakukan validasi input. Setelahnya program akan identifikasi apakah id cuti ada dalam data daftar cuti, jika tidak maka akan diarahkan untuk menginput id cuti kembali, jika ya maka akan di identifikasi username dan role, jika role adalah user maka akan ditsampilkan bahwa anda tidak bisa menghapus cuti selain milik anda kemudian diarahkan kembali ke menu. Jika tidak maka program akan menghapus data dalam daftar cuti, lalu menampilkan pengajuan cuti berhasil dibatalkan, setelahnya akan dikembalikan ke menu. <br>

  g. 5. LOGOUT <br>
    jika pilihan adalah 5 maka akan menampilkan anda berhasil logout dan program berhenti, jika tidak maka akan ditampilkan pilihan tidak ditemukan dan pengguna akan dikembalikan ke menu utama. <br>

**3. Dokumentasi Program dan Output** <br>
- Import Library <br>
<img width="177" height="29" alt="image" src="https://github.com/user-attachments/assets/8fbdf257-2856-4b7f-9bcb-f30f7d1f29e4" /> <br>

- Simpan Data Akun <br>
<img width="167" height="205" alt="image" src="https://github.com/user-attachments/assets/efc7fa85-b792-476b-a6f4-0694954c90d6" /> <br>

- 

  

  


  

  
 


