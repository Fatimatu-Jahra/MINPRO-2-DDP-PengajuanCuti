# MINPRO-2-DDP-PengajuanCuti
**MINI PROJECT 2 DASAR-DASAR PEMOGRAMAN**<br>
**NAMA: Fatimatu Jahra**<br>
**NIM: 2609116033**<br>
**KELAS: A**<br>
**TEMA: Sistem Pengajuan Cuti Karyawan**<br>

**1. Penjelasan Singkat Program**<br>
  Sebuah sistem sederhana dimana ada 2 role yaitu admin dan user, kedua role dapat menambah, melihat, mengubah, dan menghapus data, dengan catatan khusus role user tidak bisa melihat, mengubah, dan menghapus data selain miliknya sendiri. PT. FJ memiliki ketentuan jumlah hari cuti dimana jika jumlah hari cuti lebih daripada 5 hari maka status pengajuan akan otomatis ditolak.

**2. FLOWCHART**<br>
  a. Halaman Login <br>
  <img width="2524" height="4096" alt="FLOWCHART MINPRO 2-Login drawio" src="https://github.com/user-attachments/assets/ed78d4b1-662e-4798-bb02-21e7841978e2" /><br>
  Setelah program mulai, hal pertama yang dilakukan adalah inisialisasi akun dalam bentuk dictionary dan daftar_cuti dalam bentuk list untuk menyimpan data. Selanjutnya program akan menampilkan judul, lalu pengguna akan memasukkan username, apabila inputan tidak diisi maka data akan divalidasi dan menampilkan teks "input tidak boleh kosong", setelahnya pengguna akan diarahkan untuk input username kembali hingga benar. Setelah inputan telah terisi maka akan dilanjut dengan memasukkan password, sama seperti saat inputan username, pabila inputan kosoong maka program akan kembali ke masukkan username. Setelah terisi, program akan cek apakah username ada di dalam dictionary, jika tidak ada maka program akan menampilkan "username tidak ditemukann." dan kembali untuk input username. Setelah cek data username, selanjutnya dilakukan cek data password apakah sesuai dengan username yang ada di data akun atau tidak, jika tidak maka akan menampilkan "password salah." dan pengguna akan mengisi username kembali, jika ya maka program akan menampilkan login berhasil dan menampilkan menu. <br>

  b. Menu<br> 
  <img width="2448" height="4796" alt="FLOWCHART_MINPRO2_Menu drawio" src="https://github.com/user-attachments/assets/6ff6569c-e65a-4b56-bd66-70f4db2a1466" /> <br>
  Didalam tampilan menu, akan ditampilkan 5 menu dan pengguna akan diarahkan untuk menginput pilihan 1-5, jika pilihan kosong atau lebih daripada 5 maka program akan menampilkan "pilihan tidak tersedia" dan akan diarahkan ke tampilan menu lagi. Sesuai dengan pilihan, jika pengguna input 1 maka akan menampilkan program ajukan cuti, dst. <br>

  c. Ajukan Cuti <br>
   <img width="2682" height="5280" alt="FLOWCHART MINPRO 2-1 drawio (3)" src="https://github.com/user-attachments/assets/aa845401-41d9-4cfc-9c3c-a21927673295" /> <br>
 <br>
  pada menu pilihan pertama yaitu ajukan cuti, pengguna akan diminta untuk menginput id cuti, jika inputan kosong atau id cuti sudah digunakan, maka pengguna akan diarahkan untuk mengisi id cuti kembali. Ketika id cuti sudah terisi dan belum digunakan, maka program akan memproses apakah role pengguna adalah admin atau bukan, jika admin maka pengguna akan menginput username pemilik cuti, jika inputan kosong maka akan diarahin untuk mengisi lagi, program cek apakah username yang diinput ada dalam data akun, jika tidak ada maka akan diarahkan untuk mengisi lagi. Begitu seterusnya hingga penentuan status cuti, program akan cek apakah jumlah hari cuti lebih kecil daripada samadengan 5, jika ya maka status cuti diterima, jika tidak maka status cuti diterima. Setelahnya pengguna akan diarahkan kembali ke menu. <br>

  d. Lihat Riwayat Cuti <br>
  <img width="1600" height="1312" alt="FLOWCHART MINPRO 2-2 drawio" src="https://github.com/user-attachments/assets/9bac74b8-1f06-4112-9134-e81652934fea" /> <br>
  pada bagian lihat riwayat cuti, program akan identifikasi terlebih dahulu apakah pengguna memiliki role admin, jika ya maka akan menampilkan data riwayat yang berisi semua riwayat cuti, jika tidak maka akan menampilkan data sendiri. Setelahnya akan langsung diarahkan kembali ke menu. <br>

  e. Ubah Riwayat Cuti <br>
  <img width="5019" height="3306" alt="FLOWCHART MINPRO 2-3 drawio (3)" src="https://github.com/user-attachments/assets/043fcdeb-9b32-4232-bb91-72012513bebc" /> <br>
  pada bagian ubah riwayat cuti, yang pertama muncul adlah pengguna menginput id cuti yang ingin diubah, kemudian program cek apakah id cuti ada dalam daftar cuti, jika tidak maka akan dikembalikan ke masukkan id cuti, jika ya maka program akan menidentifikasi username dan role, jika role bukan user maka akan diidentifikasi lagi apakah pemilik tidak sama dengan username, jika ya maka akan menampilkan anda tiak bisa mengubah cuti selain milik adn dan kembali ke masukkan id cuti. Jika pemilik sama dengan username maka program akan menampilkan 3 pilihan menu yang ingin diubah, kemudian pengguna akan menginput piliha, jika inputan kosong atau lebih dari 3 maka akan menampilkan pilihan tidak valid dan diarahkan kembali ke menu. Jika pilihan 1 maka akan diarahkan untuk menginput nama baru kemudian validasi input, setelahnya akan ditampilkan data cuti berhasil diubah dan kembali ke menu. Jika pilihan 2 maka pengguna akan memasukkan jumlah hari baru, jika inputan kosong atau angka berubah kurang dari 0 maka pengguna akan diarahkan untuk mengisi jumlah hari baru, setelahnya akan ditampilkan bahwa data cuti berhasil diubah dan diarahkan kembali ke menu. Jika pilihan 3 maka penggun akan memasukkan alasan baru kemudian validasi input dan akan ditampilkan data cuti berhqsil diubah lalu diarahkan kembali ke menu. <br>

  f. Batalkan Pengajuan Cuti <br>
  <img width="2520" height="3952" alt="FLOWCHART MINPRO 2-4 drawio" src="https://github.com/user-attachments/assets/10e45aed-5d0a-4fa8-a952-a6ed51e82b9a" /> <br>
  pada bagian ini, pengguna akan menginput data id cuti yang ingin dihapus, kemudian dilakukan validasi input. Setelahnya program akan identifikasi apakah id cuti ada dalam data daftar cuti, jika tidak maka akan diarahkan untuk menginput id cuti kembali, jika ya maka akan di identifikasi username dan role, jika role adalah user maka akan ditsampilkan bahwa anda tidak bisa menghapus cuti selain milik anda kemudian diarahkan kembali ke menu. Jika tidak maka program akan menghapus data dalam daftar cuti, lalu menampilkan pengajuan cuti berhasil dibatalkan, setelahnya akan dikembalikan ke menu. <br>

  g. LOGOUT <br>
    jika pilihan adalah 5 maka akan menampilkan anda berhasil logout dan program berhenti, jika tidak maka akan ditampilkan pilihan tidak ditemukan dan pengguna akan dikembalikan ke menu utama. <br>

**3. Input Program** <br>
- Import Library <br>
<img width="177" height="29" alt="image" src="https://github.com/user-attachments/assets/8fbdf257-2856-4b7f-9bcb-f30f7d1f29e4" /> <br>

- Simpan Data Akun <br>
<img width="167" height="205" alt="image" src="https://github.com/user-attachments/assets/efc7fa85-b792-476b-a6f4-0694954c90d6" /> <br>

- Tampilan Judul <br>
Input <br>
<img width="228" height="20" alt="image" src="https://github.com/user-attachments/assets/801ea1f5-e779-4570-8b58-ff157c500cdc" /> <br>
Menggunakan print biasa dalam menampilkan judul program. <br>
Output <br>
<img width="232" height="17" alt="image" src="https://github.com/user-attachments/assets/9fc24687-c2de-4a6d-a963-1b4bd9910f51" /> <br>

**FUNCTION**
- Validasi Input <br>
<img width="203" height="83" alt="image" src="https://github.com/user-attachments/assets/2291108c-9a0a-4a6b-8c5b-b473a2cc0098" /> <br>
data yang diinput oleh pengguna akan disimpan dalam variable `data`, kemudian menggunakan `data.strip() == "":` untuk mengidentifikasi apabila inputan kosong setelah spasi di awal dan di akhir dihapus, jika iya maka akan menampilkan "Input tidak boleh kosong" dan meminta pengguna untuk mengisi kembali. <br>

- Validasi Input bentuk Angka <br>
<img width="290" height="73" alt="image" src="https://github.com/user-attachments/assets/358de381-7a56-4cfd-8f18-01e44174e4be" /> <br>
dalam validasi input angka, inputan disimpan dalam variable `data_angka`, ketika pengguna tidak menginput atau menginput angka kurang dari 0, maka akan ditampilkan "Input harus berupa lebih dari 0." dan pengguna akan diarahkan untuk mengisi kembali. <br>

- Login <br>
  <img width="310" height="203" alt="image" src="https://github.com/user-attachments/assets/00328138-9a2d-4b0a-b38e-5fbfef2c87b4" /> <br>
  dalam halaman login menggunakan perulangan, hal pertama yang ditampilkan adalah "halaman login" sebagai judul program, kemudian menyimpan username dalam variable `username`, kemudian password dalam variable `password`, pada bagian variable password menggunakan library pwinput agar ketika pengguna menginput password maka karakter tidak terdeteksi atau berbentuk bintang. Kemudian apabila `username` ada dalam data `akun` maka program akan menyesuaikan password sesuai dengan password yang ada pada akun dengan username tersebut, setelahnya program akan menampilkan "login berhasil!" dan menampilkan ucapan selamat datang, kemudian apabila password yang diinput tidak sesuai dengan data password pada username, maka akan ditampilkan "passsword salah." dan pengguna akan mengulang mengisi dari username. Jika username tidak ditemukan pada variable `akun` maka akan ditampilkan "username tidak ditemukan." <br

- Penentuan Status Cuti <br>
<img width="143" height="65" alt="image" src="https://github.com/user-attachments/assets/9d570c14-c5b1-442a-93f4-d74043c8dd40" /> <br>
apabila nilai pada jumlah hari lebih kecil atau sama dengan 5 maka status diterima, jika lebih maka ditolak. <br>

- Tabel <br>
<img width="328" height="144" alt="image" src="https://github.com/user-attachments/assets/ac7948bb-66c0-41c2-9bc0-c52e9ccbe391" /> <br>
jika karakter dalam data bernilai 0 atau tidak ada maka akan ditampilkan "tidak ada data cuti", maka akan dikembalikan ke program selanjutnya. Menggunakan prettytable yang disimpan pada variable `tabel`, didalamnya terdapat data daftar_cuti. <br>

- Cari Cuti <br>
<img width="155" height="49" alt="image" src="https://github.com/user-attachments/assets/a1e69a0c-ae57-4b70-9392-8a1348eadd6d" /> <br>
saya membuat function cari cuti sebab beberapa pilihan menu perlu menginput id cuti terlebih dahulu dan id cuti harus ditemukan pada data daftar cuti. Jika dta tidak ditemukan maka akan dikembalikan ke program sebelumnya. <br>

- Ajukan Cuti <br>
<img width="277" height="275" alt="image" src="https://github.com/user-attachments/assets/f48e3a1a-a56b-4acd-ac5e-ee9699e8c98f" /> <br>
dalam function ini, id cuti disimpan dalam variable `id cuti`, apabila id cuti ditemukan dalam data id cuti maka ditampilkan id cuti sudah digunakan, dan harus mengisi id cuti yang lain. Kemudian diidentifikasi apabila pengguna memiliki role admin maka tampilka masukan username pemilik cuti, dan jika pemilik cuti tidak ditemukan pada data akun maka tampilkan username karyawan tidak ditemukan, apabila ditemukan dan atau pengguna adalah pemilik yang sama dengan username maka akan dilanjutkan mengisi data nama, jumlah hari, alasan, dan status akan ditentukan dari jumlah hari.. Setelahnya data akan disimpan pada daftar cuti dengan menggunakan `.append`. <br>


- Lihat Riwayat <br>
<img width="176" height="87" alt="image" src="https://github.com/user-attachments/assets/8581e63d-30c8-40aa-8728-176482d81488" /> <br>
dalam function ini apabila pengguna memiliki role admin maka pengguna bisa memlihat daftar cuti dari semua role. apabila pengguna memiliki role selain admin dan sesuai dengan pemilik maka akan ditampilkan data sendiri. <br>

- Ubah Cuti <br>
<img width="290" height="286" alt="image" src="https://github.com/user-attachments/assets/5f9a1485-75d4-43df-9003-6ca2e12a1602" /> <br>
sama seperti program sebelumnya, yang pertama diinput adalah id cuti, jika id cuti ditemukan maka program dilanjutkan, jika tidak akan dikembalikan. Jika ditemukan dan apabila pengguna memiliki role user dan ingin mengubah id cuti selain miliknya sendiri. <br>

- Batalkan Cuti <br>
<img width="275" height="172" alt="image" src="https://github.com/user-attachments/assets/cd12f8fe-fee8-48dc-b91b-a8bfe65f30b0" /> <br>
beberapa kode sama seperti yang di atas, pada function ini menggunakan `.remove` untuk menghapus data cuti dari daftar cuti. <br>

**4. Input dan Output**
**Login**
  - Input <br>
  <img width="136" height="33" alt="image" src="https://github.com/user-attachments/assets/feff5e79-d015-46e6-b12b-0d199cd0cdb2" /> <br>
  - Output (Data ditemukan) <br>
  <img width="232" height="95" alt="image" src="https://github.com/user-attachments/assets/5d5c9422-9128-45e0-9e7a-d9be689ea31b" /> <br>
  - Output (Input username kosong) <br>
  <img width="155" height="41" alt="image" src="https://github.com/user-attachments/assets/cd6dc8e6-335c-4096-9490-a00b31b5ac25" /> <br>
  - Output (Password salah) <br>
  <img width="92" height="68" alt="image" src="https://github.com/user-attachments/assets/bf5b7542-3bab-4a5f-b852-5cfdf40367d8" /> <br>
  - Output (Role user) <br>
  <img width="161" height="163" alt="image" src="https://github.com/user-attachments/assets/8705fab5-ea1e-4894-b843-85f4ef54c321" /> <br>
  - Output (Role admin) <br>
  <img width="164" height="164" alt="image" src="https://github.com/user-attachments/assets/639762c4-9534-4bbc-b587-8b05df1b2c2c" /> <br>

  **Tampilan Menu** <br>
  - Input <br>
  <img width="168" height="72" alt="image" src="https://github.com/user-attachments/assets/68e9ce96-7106-4652-963a-67b4138f94f1" /> <br>
  - Output <br>
  <img width="163" height="92" alt="image" src="https://github.com/user-attachments/assets/2a4162f1-5214-42e8-bbf8-f7604a4a8f57" /> <br>

  **Pilihan Menu** <br>
  Input <br>
  <img width="199" height="176" alt="image" src="https://github.com/user-attachments/assets/b7fbb7df-92a2-425d-bb7e-3155cf295886" /> <br>
  1. Ajukan Cuti <br>
  - Output (role == admin, dengan kemungkinan id cuti belum digunakan dan username ada pada data akun) <br>
  <img width="231" height="109" alt="image" src="https://github.com/user-attachments/assets/fbd35ac4-70eb-4b01-a667-f5f69b06dd5c" /> <br>
  - Output (role == admin, dengan kemungkinan id cuti sudah digunakan) <br>
  <img width="185" height="56" alt="image" src="https://github.com/user-attachments/assets/da81949c-1505-4d93-a20f-e9ddb8f85456" /> <br>
  - Output (role == admin, dengan kemungkinan username tidak ditemukan) <br>
  <img width="239" height="53" alt="image" src="https://github.com/user-attachments/assets/5c361ab6-8072-49f6-95d1-eb8bdbfbc16a" /> <br>
  - Output (role == user, dengan kemungkinan id belum digunakan) <br>
  <img width="218" height="177" alt="image" src="https://github.com/user-attachments/assets/c6cadc92-6377-4b90-95da-b40449b80e61" /> <br>
  - Output (role == user, id sudah digunakan) <br>
  <img width="179" height="41" alt="image" src="https://github.com/user-attachments/assets/3e40d3b3-a4b2-4438-a0b2-99025063421c" /> <br>

  2. Lihat Riwayat Cuti <br>
  - Output (role == user) <br>
  <img width="354" height="95" alt="image" src="https://github.com/user-attachments/assets/b096a6a1-5126-4abe-ae8b-7395e4c7b7f4" /> <br>
  - Output (semua role, dengan kemungkinan tidak ada data cuti) <br>
  <img width="164" height="112" alt="image" src="https://github.com/user-attachments/assets/082c1d3a-954c-44cd-8c68-b04af390afcc" /> <br>

  3. Ubah Pengajuan Cuti <br>
  - Output (id cuti tidak ditemukan) <br>
  <img width="251" height="136" alt="image" src="https://github.com/user-attachments/assets/76787259-a160-4de7-bc20-8498482e9717" /> <br>
  - Output (role == admin, id cuti ditemukan) <br>
  <img width="256" height="83" alt="image" src="https://github.com/user-attachments/assets/e57456bd-67a2-40d8-9d37-cd96732e3374" /> <br>
  - Output (role == admin, mengubah nama) <br>
  <img width="230" height="136" alt="image" src="https://github.com/user-attachments/assets/45f11f68-ff49-433e-b125-a032cd58a45f" /> <br>
  - Output (role == admin, mengubah jumlah hari cuti) <br>
  <img width="228" height="129" alt="image" src="https://github.com/user-attachments/assets/1c3b21b4-514f-49d6-95cb-210efd6a9938" /> <br>
  - Output (role == admin, mengubah alasan) <br>
  <img width="232" height="133" alt="image" src="https://github.com/user-attachments/assets/163b010c-c78b-4486-861f-f0f27e1e87ff" /> <br>
  - Output (role == user, id cuti tidak ditemukan) <br>
  <img width="256" height="124" alt="image" src="https://github.com/user-attachments/assets/9986c8cd-78aa-45ae-8cb2-5280166d44e5" /> <br>
  - Output (role == user, id cuti ditemukan) <br>
  <img width="251" height="70" alt="image" src="https://github.com/user-attachments/assets/4d006918-2e82-416e-97ac-940048c70449" /> <br>
  - Output (role == user, mengubah nama, jumlah hari, dan alasan) <br>
  <img width="229" height="122" alt="image" src="https://github.com/user-attachments/assets/836da984-0915-4cbe-a234-fb2e0095f2d0" /> 
  <img width="233" height="122" alt="image" src="https://github.com/user-attachments/assets/a951f6ea-773a-4380-aa9d-dde26e0e2242" />
  <img width="232" height="140" alt="image" src="https://github.com/user-attachments/assets/c0c36b67-a980-46a7-a477-a4f93cc7f74f" />

  4. Batalkan Pengajuan Cuti <br>
  - Output (role == admin/user, dengan kemungkinan id cuti tidak ditemukan) <br>
  <img width="164" height="139" alt="image" src="https://github.com/user-attachments/assets/1619b4c5-1317-473b-b1e0-1d4f667b7d65" /> <br>
  - Output (role == user) <br>
  <img width="217" height="135" alt="image" src="https://github.com/user-attachments/assets/0f3ec1f8-fd88-4202-96f9-aa509bb91ee3" /> <br>
  - Output (role == admin) <br>
  <img width="221" height="140" alt="image" src="https://github.com/user-attachments/assets/75fab684-a7e9-4223-b224-90325aa5d03d" /> <br>

  5. LOGOUT <br>
  <img width="197" height="43" alt="image" src="https://github.com/user-attachments/assets/22e5cf48-2c07-468a-b8a5-03af0ef44b9a" /> <br>


  


  



  



  - 
  

  

  




  

  

  

  


  

  

  

  

  
  

  










  





- 

  

  


  

  
 


