# Tugas Kelompok PBP D04
### Anggota Kelompok

| NAMA                  | NPM           |
| ----------------------|---------------| 
| Affandi Shafwan Soleh | 2306245075    |
| Gilbert Kristian      | 2306274951    |
| Luqmanul Hakim        | 2306152191    |
| Stefanus Tan Jaya     | 2306152456    |
| Sultan Ibnu Mansiz    | 2306275840    |

### Link Deployment Aplikasi
Aplikasi Makansar dapat diakses dengan link di bawah ini.
* ##### LINK: [Makansar - Makanan Makassar](http://sultan-ibnu-makansar.pbp.cs.ui.ac.id/)

## Deskripsi Aplikasi
Makassar, sebagai salah satu kota terbesar di Indonesia, terkenal dengan ragam kuliner khasnya yang menggugah selera. 
Dengan semakin pesatnya perkembangan industri makanan dan minuman di kota ini, banyak warga lokal maupun wisatawan yang mencari informasi terkait kuliner terbaik yang bisa mereka coba. 
Namun, dengan banyaknya pilihan dan variasi harga, kualitas, serta lokasi, masyarakat sering kali kesulitan untuk menemukan tempat makan yang sesuai dengan keinginan mereka. 
Oleh karena itu, sebuah aplikasi yang mampu memberikan informasi makanan di Makassar, seperti lokasi, harga, dan rating, menjadi kebutuhan yang sangat relevan. 
Aplikasi ini tidak hanya membantu pengguna menemukan makanan yang sesuai dengan preferensi mereka, tetapi juga membantu pelaku bisnis kuliner untuk lebih mudah dikenal oleh calon pelanggan.

Aplikasi ini kami beri nama "Makansar" yang merupakan akronim dari "Makanan Makassar". Makansar adalah aplikasi panduan kuliner Makassar yang memudahkan pengguna dalam mencari dan memesan makanan. Penjual dapat mengelola produk mereka secara mandiri, sementara pembeli bisa menambahkan makanan ke favorit, melakukan pemesanan dengan fitur keranjang belanja yang lengkap, serta mengedit informasi di dashboard mereka. Pembeli juga dapat memberikan rating dan komentar pada produk, membantu pengguna lain dalam memilih makanan. Dengan fitur login khusus untuk penjual dan pembeli, aplikasi ini dirancang untuk memberikan pengalaman kuliner yang efisien dan menyenangkan.

## Daftar Modul Aplikasi

* _Login_ sebagai penjual

    Dalam aplikasi kami, pengguna dapat _login_ sebagai **penjual** atau **pembeli**. 
    Jika pengguna _login_ sebagai **penjual**, mereka hanya dapat melihat produk-produk yang telah mereka tambahkan sendiri. 
    Selain itu, penjual juga memiliki akses untuk mengedit dan menghapus produk miliknya. 
    Produk yang ditambahkan oleh penjual akan tersedia dan dapat dilihat oleh pengguna yang _login_ sebagai **pembeli**.

    ##### Dikerjakan oleh: Sultan Ibnu Mansiz 

* _Add_ dan _Remove_ ke _Favorite_ untuk pembeli

    Page _favorite_ akan menampilkan makanan _favorite_ dari masing-masing pengguna.
    Pada _page_ ini, akan ada fitur untuk membaca data makanan yang ada.  
    Kemudian, dari data tersebut terdapat fitur _add to favorite_, _remove from_ _favorite_, dan _update_ dari _top_ 3 makanan _favorite_ dari masing-masing pengguna. 
    _Top_ 3 makanan _favorite_ nantinya akan ditampilkan pada bagian atas _page_ ini.

    ##### Dikerjakan oleh: Luqmanul Hakim

* _Order_ makanan untuk pembeli

    Pembeli dapat menambahkan berbagai pilihan makanan dan minuman yang tersedia ke dalam keranjang belanja mereka. 
    Di dalam _page_ keranjang, tersedia fitur _edit_ untuk menambah atau mengurangi jumlah produk dan _delete_ untuk menghapus produk yang ingin dikeluakrkan dari keranjang.
    Pembeli juga dapat melihat ringkasan mengenai nama, jumlah, dan harga setiap produk yang dipilih, sehingga memudahkan pembeli untuk mengecek total belanja mereka.

    ##### Dikerjakan oleh: Affandi Shafwan Soleh

* Profil _Dashboard_ untuk pembeli

    Setelah pembeli berhasil _log in_, pembeli diarahkan kepada _page_ yang berisi informasi pribadinya yang terdiri dari foto profil, nama lengkap, nomor telepon, _email_, dan alamat. 
    Pembeli dapat mengedit informasi pribadinya tersebut dan melengkapi informasi yang belum terisi saat registrasi akun di awal. 
    Pembeli juga mendapat akses untuk menghapus akunnya bila dirasa sudah tidak terpakai lagi.
  
    ##### Dikerjakan oleh: Stefanus Tan Jaya

* Pemberian _rating_ & komentar pembeli

    Pada tiap produk makanan dan minuman yang tersedia, seorang pembeli dapat memberikan _rating_ dan komentar pada pilihan makanan atau minuman yang dipilihnya. 
    _Rating_ dan komentar akan dijadikan sebagai acuan oleh pembeli dalam memilih makanan atau minuman yang tersedia berdasarkan rekomendasi pembeli lain. 
    Pembeli dapat menghapus dan mengedit komentar yang telah dibuatnya.

    ##### Dikerjakan oleh: Gilbert Kristian


## Sumber _Initial Dataset_
_Dataset_ yang digunakan dalam pengembangan aplikasi **Makansar** dapat diakses melalui tautan di bawah ini. Kami mengumpulkan _dataset_ tersebut dari berbagai sumber online terpercaya, termasuk Google dan platform _e-commerce_, untuk memastikan keakuratan dan relevansi data dalam mendukung fitur-fitur aplikasi.

* ##### LINK: [Dataset Makansar](https://docs.google.com/spreadsheets/d/15Phx5eEcQyXIlRXnik7vvG9ARDdfnjWsjejs8jLbDwg/edit?usp=sharing)

## _Role_ atau Peran Pengguna
_Role_ pengguna di _website_ ini dibagi menjadi dua, yaitu **penjual** dan **pembeli**. 
Penjual dapat mengunggah ataupun menambah makanan atau minuman yang ingin mereka jual. 
Penjual dapat menghapus produk yang telah ditambahkan apabila stok habis atau tidak menginginkan untuk menjualnya lagi. 
Penjual dapat meng-_edit_ 
informasi produk yang telah ditambahkan sebelumnya.  

Pembeli dapat melihat makanan dan minuman yang tersedia di _web_. 
Pembeli juga dapat meng-_edit_ informasi pribadi dengan menggunakan fitur _dashboard_ yang tersedia di halaman utama _website_. 
Pembeli memiliki akses untuk memesan produk yang ia minati, kemudian memberikan _rating_ dan komentar pada produk yang ia pilih. 
Tidak lupa, pembeli juga dapat memiliki kendali penuh atas daftar makanan favorit mereka dengan fitur menambahkan atau menghapus makanan dari daftar tersebut.
