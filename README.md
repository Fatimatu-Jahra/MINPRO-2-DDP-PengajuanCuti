# MINPRO-2-DDP-PengajuanCuti
**MINI PROJECT 2 DASAR-DASAR PEMOGRAMMAN**<br>
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
  
 


