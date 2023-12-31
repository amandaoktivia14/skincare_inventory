# Vivi's Skincare Inventory
`Amanda Oktivia Sharfina 2206830076
(PBP-B)`

## Tugas 2
>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 - [x] Membuat sebuah proyek Django baru.

 Pada langkah awal, saya membuat direktori lokal baru dan juga repositori GitHub baru. Selanjutnya, saya menghubungkan repositori lokal dengan repositori di GitHub dengan perintah "git branch -M main" untuk menciptakan branch utama, dan menggunakan perintah "git remote add origin <URL_REPO>" untuk mengaitkan repositori lokal dengan repositori di GitHub.

Kemudian, saya membuat lingkungan virtual dengan menjalankan perintah "python -m venv env" dan mengaktifkannya dengan perintah "source env/bin/activate". Dalam keadaan lingkungan virtual yang aktif, saya menambahkan file "requirements.txt" sebagai daftar dependensi yang akan digunakan dalam proyek ini. Saya menginstal semua dependensi dari file "requirements.txt" dengan perintah "pip install -r requirements.txt".

Setelah itu, saya membuat proyek Django baru dengan nama "skincare-inventory" dengan menjalankan perintah "django-admin startproject skincare_inventory ..".

Langkah selanjutnya adalah mengonfigurasi proyek dengan menambahkan tanda bintang (*) pada variabel "ALLOWED_HOSTS" di file "settings.py" untuk memberikan izin akses kepada semua host.

 - [x]  Membuat aplikasi dengan nama `main` pada proyek tersebut.

Pada langkah ini, saya menginisialisasi struktur inti proyek dengan menambahkan direktori "main" ke dalam repositori proyek menggunakan perintah "python3 manage.py startapp main". Selanjutnya, saya memasukkan folder "main" ke dalam daftar aplikasi yang terdaftar dalam variabel "INSTALLED_APPS" di dalam file "settings.py" untuk mendaftarkannya ke dalam proyek.

 - [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

Saya sebagai developer akan mulai mendefinisikan rute URL aplikasi utama dengan menambahkan path ke dalam variabel urlpatterns pada file urls.py. Path tersebut akan terdiri dari informasi tentang route, function yang ada di dalam file views.py, dan juga parameter name. Selanjutnya, saya akan mengonfigurasi routing URL proyek dengan menambahkan path yang mencakup route dan fungsi include ke dalam variabel urlpatterns. Fungsi include ini sangat berguna karena memungkinkan saya untuk mengimpor rute URL dari aplikasi main ke dalam file urls.py proyek, sehingga proyek ini dapat berjalan dengan baik.


 - [x] Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut wajib sebagai berikut.
    + `name` sebagai nama *product* dengan tipe `CharField`.
    + `category` sebagai kategori *product* dengan tipe `CharField`.
    + `price` sebagai harga *product* dengan tipe `IntegerField`.
    + `amount` sebagai jumlah *product* dengan tipe `IntegerField`.
    + `description` sebagai deskripsi *product* dengan tipe `TextField`.
        Saya sebagai developer, membuat model yang berisi beberapa atribut bersama dengan atribut tambahan. Salah satunya adalah atribut "category" yang digunakan sebagai kategori product dengan tipe data CharField, atribut "price" yang berfungsi sebagai harga product dengan tipe data IntegerField, dan lain-lain. Setelah saya berhasil mendefinisikan semua atribut model tersebut, langkah selanjutnya adalah melakukan migrasi model ke dalam database. Untuk melakukannya, saya menjalankan perintah "python3 manage.py makemigrations" untuk membuat file migrasi yang diperlukan. Setelah file migrasi tersebut dibuat, langkah terakhir adalah menerapkannya ke dalam database dengan menjalankan perintah "python3 manage.py migrate."


 - [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

    Saya sebagai developer pertama-tama mengimpor fungsi "render" dari modul "django.shortcuts" untuk digunakan dalam proses rendering tampilan "main_page.html". Selanjutnya, mendefinisikan fungsi "show_main" dengan parameter "request". Tujuan dari fungsi ini adalah untuk mengatur permintaan HTTP dan menghasilkan tampilan yang sesuai dengan permintaan tersebut.

    Setelah itu, lanjutkan dengan menambahkan data seperti "name", "class", dan "product" ke dalam konteks yang ada dalam fungsi "show_main". Konteks ini akan digunakan untuk mengirimkan data ke tampilan HTML yang akan ditampilkan.

    Langkah terakhir, saya menggunakan perintah "return render(request, "main.html", context)" untuk menampilkan tampilan HTML di web server. Dengan cara ini, saya memastikan bahwa halaman "main_page.html" akan dirender dengan benar sesuai dengan konteks yang telah saya tentukan sebelumnya.


 - [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

    Pada langkah awal, saya sebagai developer mengawali dengan mengimpor modul "path" dari "django.urls" serta fungsi "show_main" dari berkas "views.py". Kemudian, saya memberikan sebuah label "app_name" yang saya namakan "main" untuk memberikan identitas yang unik pada pola URL dalam aplikasi ini. Setelah itu, langkah berikutnya adalah menambahkan path ke dalam variabel "urlpatterns", yang mencakup informasi mengenai rute, fungsi "show_main", dan parameter "name".

 - [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

    Setelah semua poin dalam checklist telah selesai, developer melakukan push semua perubahan yang telah dibuat ke dalam GitHub. Pertama, developer menjalankan perintah git add . untuk mengambil seluruh perubahan yang belum di-stage. Kemudian developer menjalankan perintah git commit -m "<komentar>" dan git push origin main. Setelah berhasil melakukan push semua perubahan ke repositori GitHub,lanjutkan dengan proses deploy aplikasi menggunakan layanan Adapatable.io. Saya menggunakan repositori GitHub proyek "skincare_inventory" dan branch "main." Selanjutnya, saya memilih Python App Template dan mengkonfigurasi PostgreSQL sebagai database yang akan digunakan. Saya juga menyesuaikan versi Python yang akan digunakan di dalam lingkungan virtual, yaitu versi 3.10. menetapkan perintah python manage.py migrate && gunicorn skincare_inventory_App.wsgi pada bagian start command, memasukkan nama aplikasi, yaitu skincare_inventory, mencentang opsi HTTP Listener on PORT, dan klik Deploy.


>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

    ![Diagram](static/S__2965506.jpg)


>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

- [x] Kita memanfaatkan virtual environment untuk mengatur dan membatasi dependensi yang diperlukan oleh proyek Python agar terisolasi. Dependensi ini merujuk kepada komponen-komponen atau modul-modul yang diperlukan oleh perangkat lunak, seperti library, framework, atau package tertentu. Setiap proyek biasanya memiliki spesifikasi yang unik. Salah satu keuntungan utama adalah kita dapat menginstal versi-dependensi yang sesuai dengan kebutuhan proyek dalam virtual environment tertentu tanpa mempengaruhi instalasi Python global pada sistem.

Pemanfaatan virtual environment memiliki kepentingan signifikan dan memberi berbagai keuntungan, seperti kemudahan dalam manajemen, stabilitas, portabilitas, dan isolasi. Meskipun demikian, membangun aplikasi web berbasis Django masih memungkinkan tanpa menggunakan virtual environment. Namun, ada beberapa aspek yang perlu diperhatikan agar dapat menghindari potensi masalah. Jika Anda menginstal paket yang sama untuk dua aplikasi web Django berbeda, mungkin akan muncul konflik paket. Selain itu, ketika Anda ingin mendeploy aplikasi web Django ke server, Anda harus memastikan bahwa semua paket yang dibutuhkan telah terpasang di server tersebut. Inti dari permasalahan ini terletak pada keberadaan berkas requirements.txt. Ketika Anda sudah menginisialisasi lingkungan virtual, requirements.txt menjadi alat yang sangat berguna bagi penyedia layanan hosting untuk mengelola dan menjalankan aplikasi Django dengan lebih efisien, aman, dan konsisten dalam lingkungan hosting.

>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

- [x] Arsitektur desain Model View Controller memecah kode menjadi tiga bagian utama: Model, View, dan Controller.

    Model: Bagian ini berisi logika bisnis untuk mengambil dan mengelola data, berkomunikasi dengan pengontrol, berinteraksi dengan database, dan melakukan pembaruan terhadap tampilan.

    View: User Interface mengandung elemen-elemen seperti HTML, CSS, dan XML. Terkadang, tampilan berinteraksi dengan pengontrol dan terkadang juga berhubungan dengan model. Melalui pengontrol, data dinamis kadang-kadang melewati beberapa tampilan.

    Controller: Komponen ini sering kali dikenal sebagai Aktivitas atau Fragmen. Pengontrol ini menjalin komunikasi antara tampilan dan model. Pengontrol menerima masukan pengguna dari layanan tampilan atau REST. Selanjutnya, pengontrol mengambil data dari model, memproses permintaan, dan meneruskannya ke tampilan.

- [x] MVP populer karena memberikan modularitas, kemampuan pengujian, dan basis kode yang lebih bersih dan mudah dipelihara yang membantu meningkatkan logika presentasi kode.
        
        Model: Lapisan untuk menyimpan data. Ini menangani logika domain (aturan bisnis aktual) dan bertanggung jawab untuk berkomunikasi dengan database dan lapisan jaringan.

        View: Ini adalah lapisan UI (antarmuka pengguna). Ini menyediakan visualisasi data dan digunakan untuk melacak tindakan pengguna sehingga kami dapat memberi tahu penyaji.

        Presenter: Dibutuhkan data dari model dan menerapkan logika UI untuk menentukan apa yang harus kita tampilkan kepada pengguna. Ini berguna karena mengelola status tampilan dan mengambil tindakan sesuai dengan notifikasi yang dimasukkan pengguna dari tampilan.

- [x] Pola MVVM memiliki beberapa kesamaan dengan pola desain MVP di mana ViewModel mewarisi peran presenter. Kami mengatasi kekurangan pola MVP dengan MVVM. Model ini menyarankan pemisahan logika presentasi data (tampilan atau UI) dari bagian logika bisnis inti aplikasi. 

        Model: Lapisan ini terutama bertanggung jawab atas abstraksi sumber data. Model dan ViewModel bekerja sama untuk mendapatkan dan menyimpan data.

        View: Lapisan ini bertujuan untuk menginformasikan model tampilan tindakan pengguna. Lapisan ini memonitor ViewModel dan tidak mengandung logika aplikasi apa pun.

        ViewModel: Mengekspos aliran data yang terkait dengan tampilan. Ini juga bertindak sebagai penghubung antara model dan tampilan.
    
 - [x] Letak perbedaannya antara MVC, MVT, dan MVVM adalah komponen selain Model dan View, yaitu Controller dalam MVC, Template dalam MVT, dan ViewModel dalam MVVM.

## Tugas 3
>1. Apa perbedaan antara form POST dan form GET dalam Django?
 - [x]
Dalam form POST, informasi dikirimkan melalui tubuh permintaan HTTP, sehingga tidak terlihat dalam URL. Ini sangat berguna untuk mengirim data yang perlu dijaga kerahasiaannya, karena tidak mudah terlihat oleh pengguna. Form POST lebih cocok digunakan untuk mengirimkan data sensitif, seperti kata sandi atau informasi pribadi. Selain itu, tidak ada batasan praktis terkait panjang data yang dapat dikirimkan dengan metode POST. Form POST digunakan ketika ingin mengirimkan data yang akan diolah oleh server, seperti mengirim formulir, melakukan permintaan AJAX, atau melakukan operasi server lainnya, seperti menambahkan, mengedit, atau menghapus data.

Di sisi lain, dalam form GET, data dikirimkan sebagai bagian dari URL. Data ini muncul dalam string query URL dan dapat dilihat oleh semua orang yang melihat URL tersebut. Form GET lebih sesuai untuk permintaan yang tidak memiliki dampak besar dan hanya digunakan untuk membaca data. Namun, form GET bukan pilihan yang aman ketika ingin mengirimkan data yang bersifat sensitif. Selain itu, terdapat batasan pada panjang URL yang bisa diatasi oleh browser dan server, sehingga tidak cocok digunakan untuk mengirim data yang sangat besar. Metode GET biasanya digunakan untuk mengambil data dari server, seperti menampilkan halaman web, melakukan pencarian, atau mengirimkan parameter dalam URL.

>2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
 - [x] 1. XML (eXtensible Markup Language) adalah bahasa yang mengadopsi sintaksis yang ketat dan menggunakan tag untuk merinci struktur data dan hierarkinya. Format ini diterapkan dalam berbagai konteks, termasuk konfigurasi, pertukaran data, penggunaan dalam protokol SOAP (Simple Object Access Protocol) dalam layanan web, dan lain sebagainya. XML memberikan dukungan yang kuat untuk validasi skema, komentar, dan metadata.

2. JSON (JavaScript Object Notation), di sisi lain, digunakan untuk pertukaran data dan merepresentasikan struktur data, serupa dengan XML, tetapi dalam format yang lebih ringkas dan mudah dibaca oleh manusia serta mudah diproses oleh mesin. JSON menggunakan format yang lebih kompak dengan objek yang mudah dibaca dan dapat dihasilkan oleh banyak bahasa pemrograman. Format JSON digunakan dalam berbagai aplikasi, termasuk pengembangan RESTful API, komunikasi antara server dan klien web, konfigurasi, serta pertukaran data antar bahasa pemrograman. Walaupun JSON tidak memiliki dukungan untuk validasi skema seperti XML, hal ini membuatnya lebih sederhana dan efisien dalam penggunaan sehari-hari.

3. HTML (Hypertext Markup Language) digunakan untuk membuat tampilan halaman web dan menentukan tata letak elemen-elemen di browser web. HTML juga menggunakan sintaksis yang mirip dengan XML, mengandung tag yang mendefinisikan elemen-elemen seperti judul, paragraf, gambar, dan tautan dalam sebuah dokumen web. HTML memiliki kemampuan untuk menciptakan tampilan grafis yang interaktif di browser dan sering digunakan bersama dengan CSS (Cascading Style Sheets) dan JavaScript untuk menciptakan pengalaman pengguna yang interaktif di web.

>3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern? 
 - [x] JSON adalah sebuah format data yang sangat mudah dibaca oleh manusia dan memiliki sintaksis yang ringkas. Salah satu keunggulan utama JSON adalah ukuran data yang kecil, sehingga dapat mengurangi beban pada jaringan saat data dikirimkan antar aplikasi atau perangkat. JSON digunakan untuk hampir semua bahasa pemrograman, membuatnya menjadi pilihan yang sangat fleksibel untuk pertukaran data, selain itu juga mendukung struktur data yang bersarang dan kompleks, memungkinkan representasi data yang lebih kompleks seperti objek dalam objek atau array dalam objek hal ini memudahkan pengelolaan data yang kompleks dalam aplikasi. JSON juga memiliki kemampuan untuk mendukung pembaruan parsial, yang berarti Anda dapat mengirimkan hanya bagian-bagian tertentu dari data yang berubah, mengoptimalkan penggunaan bandwidth. Hal ini sangat berguna dalam aplikasi yang mengharuskan pengiriman data secara berkala, JSON telah menjadi standar dalam desain RESTful API, memudahkan integrasi antar layanan web.

>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 - [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

    Sebelum developer mengimplementasikan Skeleton sebagai kerangka Views, langkah pertama yang harus dilakukan adalah mengubah fungsi urlpatterns pada file urls.py. Perubahan ini melibatkan mengganti path dari "main/" menjadi path yang kosong (''). 

    Selanjutnya, developer perlu membuat direktori "templates" pada root folder proyek, yang akan berisi file base.html. File ini akan berperan sebagai template untuk semua file HTML dalam aplikasi ini. Untuk mendaftarkan template tersebut dalam proyek, developer akan menambahkannya ke variabel TEMPLATES pada file settings.py, dengan mengatur BASE_DIR.

    Setelah itu, developer akan melakukan penyesuaian pada isi file main.html agar dapat diintegrasikan dengan template base.html. Setelah file HTML telah disesuaikan, langkah berikutnya adalah pembuatan formulir input data untuk menampilkan item-data pada HTML. Developer akan membuat file forms.py dalam folder "main" agar proyek dapat menerima data item baru. Pada file forms.py tersebut, developer akan menggunakan objek "Product" yang di-import dari file models dan akan membuat class "ProductForm". Developer akan mengisi list fields pada "ProductForm" dengan nama-nama atribut dalam bentuk string yang akan diinput oleh pengguna saat membuat Item, seperti "name", "price", "description", "category", "amount". Setelah itu, developer akan mengimpor "ProductForm" dari file forms.py ke dalam file views.py bersama dengan beberapa import lainnya. Import tersebut akan digunakan dalam fungsi "create_product", yang bertujuan untuk membuat formulir yang memungkinkan pengguna untuk menambahkan data produk secara otomatis saat data di-submit melalui form.

    Selanjutnya, developer akan mengubah fungsi "show_main" pada file views.py dengan menambahkan variabel "products" yang akan diisi dengan semua instance dari objek "Product" yang ada di dalam database, menggunakan "Product.objects.all()". Hasilnya, "products" akan dimasukkan ke dalam dictionary "context". Developer akan mengimpor fungsi "create_product" ke dalam file urls.py dalam folder "main" dan akan menambahkan path URL-nya ke dalam urlpatterns. Setelah URL tersebut ditambahkan, developer akan membuat file "create_product.html" dalam folder "main/templates" untuk menampilkan form pembuatan product kepada pengguna. Terakhir, developer akan menambahkan kode pada file "main.html" agar dapat menampilkan tabel yang berisi item-item yang telah dibuat oleh pengguna.

 - [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

    Pada tahap ini, developer telah membuat serangkaian fungsi views yang bertujuan untuk mengakses dan menampilkan data yang telah disimpan dalam aplikasi. Data ini dapat dilihat dalam beberapa format, seperti HTML, XML, dan JSON. Selama proses ini, developer telah mengimpor dua modul penting, yaitu HttpResponse untuk mengirimkan respons ke web, dan serializers untuk membantu dalam menghasilkan data dengan format yang sesuai.

    Setelah mengimpor modul yang diperlukan, developer telah membuat empat fungsi baru selain fungsi "show_main" (yang digunakan untuk menampilkan data dalam format HTML). Empat fungsi tersebut adalah "show_xml," "show_json," "show_xml_by_id," dan "show_json_by_id." Setiap fungsi ini mengembalikan respons HttpResponse dengan parameter yang sesuai, sesuai dengan format data yang diminta. Untuk menciptakan format data yang sesuai, developer menggunakan metode serialize.

 - [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 
    Untuk semua fungsi "show" yang telah ditambahkan, pastikan untuk mengimpor fungsi-fungsi tersebut ke dalam file urls.py yang berada dalam folder "main". Setelah mengimpor fungsi-fungsi tersebut, tambahkan path untuk masing-masing fungsi ke dalam variabel urlpatterns. Dengan langkah ini, pengguna sekarang memiliki kemampuan untuk mengakses URL dengan berbagai format seperti HTML, XML, dan JSON, baik menggunakan aplikasi seperti Postman ataupun melalui browser.
    
 - [x] Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![XML](static/xml.png)

![XML/1](static/xml%3A1.png)

![JSON](static/json.png)

![JSON/1](static/json%3A1.png)

![Localhost](static/LH8000.png)

 - [x] Melakukan add-commit-push ke GitHub

## Tugas 4
>1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?

 - [x] UserCreationForm adalah sebuah bentuk form yang disediakan oleh Django untuk menyederhanakan proses pembuatan user baru dalam aplikasi web. Form ini digunakan untuk mengumpulkan informasi yang dibutuhkan dari user saat mereka mendaftar atau membuat akun baru di situs web Anda. Form ini biasanya digunakan bersama dengan model bawaan Django User, yang menyimpan informasi pengguna seperti username, password, email, dan sebagainya.

 - [x] Kelebihan dari penggunaan UserCreationForm dalam Django:

    1. Kemudahan Penggunaan: UserCreationForm menyediakan semua logika yang diperlukan untuk membuat formulir pendaftaran pengguna. Pengembang hanya perlu mengimpor dan menggunakannya dalam tampilan Django, tanpa harus menulis kode form dari awal.

    2. Validasi Terintegrasi: Form ini sudah dilengkapi dengan validasi terintegrasi untuk memastikan bahwa informasi yang dimasukkan oleh pengguna sesuai dengan aturan yang ditetapkan, seperti memeriksa kekuatan kata sandi, kelengkapan alamat email, dan sebagainya.

    3. Kompatibilitas dengan Model User: UserCreationForm dirancang untuk berfungsi dengan model pengguna bawaan Django (User model). Hal ini membuatnya sangat mudah untuk mengintegrasikan pendaftaran pengguna dengan basis data Django.

>2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?

- [x] Autentikasi : Proses verifikasi identitas pengguna untuk memastikan bahwa yang mengakses website atau sistem adalah orang yang sesuai atau sudah terdaftar. Dalam proses ini user diharapkan login dengan memasukkan username dan password yang sesuai.

Otorisasi : Proses yang menentukan diizinkannya atau tidak penggunayang telah melewati autentikasi. Hal ini berkaitan dengan hak akses atau izin yang dimiliki oleh user dalam website atau sitem yang mau diakses. Otorisasi akan menentukan apa yang bisa mereka lakukan dalam aplikasi, misalnya, apakah mereka dapat mengedit profil mereka, mengakses halaman tertentu, atau hanya dapat membaca konten.

- [x] Keduanya sangat penting untuk memastikan hanya user sah yang dapat mengakses website atau sistem dan membatasi akses ke tindakan atau informasi tertentu, hal ini tentunya berguna untuk membantu menjaga keamanan data dan sumber daya.

>3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

- [x] Cookies adalah data kecil yang disimpan pada perangkat klien. Umumnya dalam peramban web oleh server aplikasi web ketika pengguna berinteraksi dengan situs web, Cookies bertugas menyimpan informasi yang dapat diakses oleh server saat klien melakukan permintaan selanjutnya. 

- [x] Dalam aplikasi web, Cookies dimanfaatkan untuk mengelola sesi pengguna, menyimpan preferensi pengguna, melacak aktivitas pengguna, dsb.

- [x] Django menggunakan cookies untuk mengelola data sesi pengguna dengan bantuan modul django.contrib.sessions.

>4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

- [x] Menggunakan cookies dalam pengembangan web aman jika diterapkan dan dipelihara dengan benar. Namun terdapat beberapa resiko potensial yang perlu diwaspadai yakni: 

    1. Potensi Pelanggaran Privasi: Cookies dapat digunakan untuk melacak perilaku pengguna di seluruh situs web dan dalam beberapa kasus, bahkan di seluruh internet. Hal ini dapat membahayakan privasi pengguna jika data yang dikumpulkan disalahgunakan. 

    2. Cross-Site Scripting (XSS): Jika suatu situs web rentan terhadap serangan XSS, penyerang dapat menyisipkan skrip berbahaya dalam cookie pengguna. Kemudian, skrip ini dapat dijalankan di peramban pengguna saat mereka mengakses situs web tersebut, yang dapat mengancam keamanan pengguna.

    3. Cross-Site Request Forgery (CSRF): Cookies yang digunakan untuk autentikasi dan otorisasi dapat menjadi sasaran serangan CSRF jika tidak diatur dengan benar. Serangan CSRF dapat memengaruhi pengguna yang sudah diautentikasi dan memungkinkan penyerang untuk melakukan tindakan atas nama pengguna tersebut tanpa izin.

>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

    Developer telah melakukan beberapa tindakan dalam pengembangan situs web:

    1. Register: Developer membuat fungsi `register` yang menggunakan `UserCreationForm` untuk mengatur pembuatan akun pada situs web. Ini memungkinkan pengguna untuk mendaftar dan membuat akun baru.

    2. Login: Developer juga membuat fungsi `login_user` untuk mengelola proses otentikasi pengguna. Fungsi ini memungkinkan pengguna untuk melakukan login dengan mengidentifikasi diri mereka dengan username dan password.

    3. Logout: Developer memiliki fungsi `logout_user` yang memungkinkan pengguna untuk keluar atau logout dari halaman mereka.

    Dalam berkas views.py dan dengan mendaftarkan rute URL dalam daftar urlpatterns pada berkas main/urls.py, developer telah memungkinkan user untuk mengakses halaman melalui tautan. Selanjutnya, developer menambahkan dekorator @login_required pada fungsi show_main agar hanya user yang telah melakukan login yang dapat mengakses halaman tersebut.

    Untuk memungkinkan user melihat data dalam format HTML, developer membuat dua template baru, yaitu register.html untuk melakukan pendaftaran pengguna baru dan login.html untuk masuk ke halaman pengguna yang telah ada. Developer juga melakukan modifikasi pada fungsi show_main dan template main.html agar hanya item yang dibuat oleh pengguna yang saat ini sedang login yang dapat terlihat. Selain itu, pada template main.html, developer menambahkan tombol logout yang memungkinkan pengguna untuk keluar dari halaman pengguna mereka.

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

    Pada halaman refister, Developer membuat dua akun:

    1. Akun pertama memiliki username "amandaos" dan password "vivi5678".
    2. Akun kedua memiliki username "sharfeenna" dan password "vivi1234".

    Selanjutnya, developer meng-input tiga buah product untuk setiap pengguna yang telah dibuat.

- [x] Menghubungkan model Product dengan User.

    Developer melakukan penghubungan antara model "Product" dengan model "User" agar setiap product yang dibuat memiliki atribut user yang mengidentifikasikan siapa yang membuat product tersebut. Ini dilakukan dengan menambahkan atribut "user" ke dalam model "Product" menggunakan metode "ForeignKey" untuk menghubungkannya dengan model "User". Setelah itu, developer menambahkan filter berdasarkan pengguna pada fungsi "show_main" sehingga yang ditampilkan hanyalah product yang telah dibuat oleh pengguna tertentu. Terakhir, developer melakukan migrasi baru pada proyek untuk menyimpan semua perubahan yang dilakukan pada berkas "models.py".

- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

    Developer melakukan beberapa perubahan pada fungsi "show_main" dan template "main.html" untuk dapat menampilkan informasi tentang user yang saat ini sedang login dan juga mencantumkan waktu terakhir kali login. Dalam fungsi "login_user," developer menambahkan logika untuk membuat cookie bernama "last_login" yang akan mencatat waktu terakhir user melakukan login. Selanjutnya, developer memasukkan data ini ke dalam konteks yang akan digunakan dalam fungsi "show_main." Selain itu, developer juga menambahkan kode dalam fungsi "logout_user" untuk menghapus cookie "last_login" saat user melakukan logout. Terakhir, developer menambahkan teks pada template "main.html" agar dapat menampilkan kepada pengguna kapan mereka terakhir kali melakukan login.

- [x] Lakukan add-commit-push ke GitHub repository.


## Tugas 5
>1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya

- [x] Element Selectror adalah jenis selektor CSS yang digunakan untuk menargetkan elemen dalam HTML berdasarkan jenis tagnya. Setiap jenis selektor CSS memiliki kegunaan dan penggunaan yang berbeda, tergantung pada kebutuhan desain dan struktur HTML yang sedang digunakan.

- [x] 
    1. Selektor Elemen (Tag) 
    Manfaat = Selektor ini digunakan untuk merujuk pada semua elemen HTML yang memiliki jenis tag tertentu. Ini adalah jenis selektor yang sangat umum dan mempengaruhi semua elemen yang cocok dengan jenis tag tersebut.

    Waktu = Selektor elemen sangat berguna ketika Anda ingin menerapkan gaya yang serupa ke semua elemen yang memiliki jenis tag yang sama. Sebagai contoh, dapat menggunakan selektor elemen cocok untuk mengatur gaya default untuk semua paragraf (<p>) atau semua judul level 1 h1 di halaman web.

    2. Selektor Universal (*)
    Manfaat = Selektor ini memilih semua elemen di dalam dokumen HTML. Ini merupakan pilihan yang sangat kuat dan bisa digunakan untuk mengatur gaya default atau menghapus margin/padding di seluruh halaman.

    Waktu = Penggunaan selektor ini harus dilakukan dengan hati-hati karena dapat berdampak pada semua elemen dalam halaman. Sebaiknya digunakan untuk mengatur reset CSS atau mengatur gaya default di tingkat tinggi.

    3. Selektor ID (#id)
    Manfaat = Selektor ini digunakan untuk memilih elemen berdasarkan atribut id yang unik. Ini memberikan kemampuan untuk secara khusus menargetkan dan merujuk pada elemen tertentu dalam dokumen.

    Waktu = Selektor ini berguna ketika Anda perlu mengatur gaya untuk satu elemen individual yang memiliki atribut id yang unik. Selain itu, dalam konteks JavaScript, selektor ini digunakan untuk merujuk ke elemen tertentu yang dibutuhkan.

    4. Selektor Kelas (.class)
    Manfaat = Selektor ini berguna untuk memilih elemen berdasarkan atribut class. Ini ideal untuk menerapkan gaya serupa pada sejumlah elemen.

    Waktu = Penggunaan selektor ini sangat tepat ketika Anda ingin menerapkan gaya yang serupa pada beberapa elemen yang memiliki atribut class yang sama atau ketika Anda ingin menambahkan perilaku JavaScript ke elemen-elemen serupa.

    5. Selektor Atribut ([attribute]) 
    Manfaat = Selektor ini memberikan Anda kemampuan untuk memilih elemen berdasarkan atribut-atribut HTML mereka, seperti href, src, atau bahkan atribut kustom yang Anda buat sendiri.

    Waktu = Seletor ini berguna ketika Anda ingin memilih elemen berdasarkan atribut tertentu. Sebagai contoh, Anda dapat menggunakannya untuk mengatur gaya untuk semua tautan eksternal (elemen `<a>` dengan atribut `href` yang merujuk ke luar).

>2. Jelaskan HTML5 Tag yang kamu ketahui (<...>).
- [x] html = Elemen root yang digunakan sebagai awalan dan akhiran dari seluruh dokumen HTML.
- [x] head = Elemen untuk mengikutsertai informasi meta serta judul web, menghubungkan dokumen dengan berkas eksternal (stylesheet dan skrip JavaScript).
- [x] link = Tag untuk menghubungkan dokumen HTML dengan berkas eksternal (stylesheet CSS)
- [x] title = Tag untuk menandai judul dari halaman weh yang akan ditampilkan pada bilah judul browser.
- [x] meta = Elemen untuk menyediakan informasi meta (deskripsi halaman, karakter encoding, dll) kepada user.
- [x] style = Elemen untuk menyeting atau menentukan gaya tampilan halaman web denggunakan CSS(Cascading Style Sheets) secara internal.
- [x] script = Tag untuk menyisipkan skrip JavaScript dalam halaman web.
- [x] body = Elemen yang berisikan seluruh konten yang ditampilkan dalam web (gambar, vidio, teks, dll).
- [x] div = Elemen untuk mengatur dan mengelompokkan konten dalam sebuah blok yang tampilannya dapat diubah dengan CSS.
- [x] h1...h6 = Tag untuk menentukan tingkat kepentingan judul halaman web, (h1=terbesar dan utama, h6=terkecil).
- [x] p = Tag untuk menampilkan paragraf teks.
- [x] a = Tag untuk membuat tautan/hyperlink ke halaman web atau berkas lain.
- [x] img = Elemen untuk menampilkan gambar pada halaman web.
- [x] table, tr, th, td = Tag untuk membuat tabel dan elemen-elemen di dalamnya. 
- [x] ul, ol, li = Digunakan untuk membuat daftar tak terurut (unordered list) dan daftar terurut - (ordered list) serta elemen-elemen dalam daftar tersebut
- [x] form, input, textarea, button = Tag untuk membuat formulir dan elemen dalam formulir(kotak input, area teks, tombol submit).
- [x] footer, header, nav, section, article = Tag untuk mengorganisir konten halaman web menjadi bagian-bagian yang lebih terstruktur(header, footer, dan artikel).
- [x] canvas = Elemen untuk menggambar grafis atau animasi menggunakan JavaScript.
- [x] video & audio = Tag untuk menyematkan video dan audio ke dalam halaman web.
- [x] svg = Tag untuk menyisipkan grafik vektor dalam format SVG (Scalable Vector Graphics) ke dalam halaman web.

>3. Jelaskan perbedaan margin dan padding.
- [x] Margin
- Mengacu pada kesenjangan antara batas dua buah elemen
- Berkaitan dengan celah ruang di luar elemen
- Elemen internal(background) tidak mempengaruhi margin
- Dapat diotomatisasi
- Bilangan bulat adalah nilai numerik margin
- Nilai margin mengggunakan properti invers(penurunan nilai akan meningkatkan garis margin, dan sebaliknya)

- [x] Padding
- Mengacu pada ruang antara konten suatu elemen dan batasnya
- Berkaitan dengan kesenjangan ruang dalam suatu elemen
- Elemen internal apapun mempengaruhi padding(background)
- Otomatisasi tidak tersedia
- Hanya bilangan real positif yang memenuhi syarat padding
- Nilai padding digunakan untuk mengontrol ukuran elemen

>4. Jelaskan perbedaan CSS Tailwind dan Bootstrap, kapan sebaiknya menggunakan Bootstrap dibanding Tailwind? dan sebaliknya.

- [x] Bootstrap adalah kerangka kerja yang sudah mapan, banyak digunakan yang menyediakan kumpulan komponen dan gaya pra-desain yang mudah disesuaikan . Bootstrap mengikuti pendekatan pengembangan web yang lebih tradisional, di mana kelas digunakan untuk menerapkan gaya pada elemen HTML. Bootstrap memiliki komunitas yang besar dan dokumentasi yang lengkap, sehingga memudahkan pengembang untuk mencari dukungan dan sumber daya. 
 
- [x] Tailwind adalah kerangka kerja lebih baru yang mengadopsi pendekatan CSS yang berfokus pada utilitas. Kerangka kerja ini menyediakan kelas-kelas yang dapat digunakan untuk menerapkan gaya-gaya tertentu pada elemen, sehingga memungkinkan fleksibilitas dan penyesuaian yang lebih besar. Pengembang dapat dengan mudah menggabungkan dan memodifikasi kelas-kelas tersebut untuk menciptakan gaya-gaya unik. Tailwind juga memiliki ukuran file yang lebih kecil dibandingkan dengan Bootstrap, yang dapat menghasilkan waktu muat yang lebih cepat untuk situs web. 
 
- [x] Pilihan antara Bootstrap dan Tailwind tergantung pada persyaratan dan preferensi proyek yang spesifik. Jika Anda membutuhkan cara yang cepat dan mudah untuk membuat situs web responsif dengan komponen-komponen pra-desain, maka Bootstrap mungkin menjadi pilihan yang lebih baik . Bootstrap cocok untuk proyek-proyek yang membutuhkan pendekatan pengembangan web yang lebih tradisional dan di mana penyesuaian bukanlah prioritas utama. Di sisi lain, jika Anda lebih menyukai pendekatan yang lebih fleksibel dan dapat disesuaikan dalam styling, maka Tailwind mungkin lebih cocok, kerangka kerja ini memungkinkan kontrol yang lebih detail terhadap gaya-gaya dan memudahkan pembuatan desain-desain unik. Tailwind cocok untuk proyek-proyek yang membutuhkan penyesuaian yang ekstensif dan di mana pendekatan CSS yang berfokus pada utilitas sesuai dengan alur kerja pengembangan.  
  
Referensi:
Rohandi, M., Husain, N., & Bay, I. (2018). Pengembangan mobile-assisted language learning menggunakan user centered design. Jurnal Nasional Teknik Elektro Dan Teknologi Informasi (Jnteti), 7(1). https://doi.org/10.22146/jnteti.v7i1.397

>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Menambahkan fitur Delete, Edit untuk product dalam tabel

Hal pertama yang dilakukan dalam membuat fitur Edit ialah membuat fungsi edit_product yang menerima parameter request dan id_product dalam file views.py pada subdirektori main. 

    def edit_product(request, id_product):
        # Get product berdasarkan ID
        product = Product.objects.get(pk = id_product)

        # Set product sebagai instance dari form
        form = ProductForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            # Simpan form dan kembali ke halaman awal
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)


Selanjutnya membuat berkas HTML baru pada folder main/templates dengan nama edit_product.html yang berisikan:

    <h1>Edit Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Product"/>
                </td>
            </tr>
        </table>
    </form>
    {% endblock %}


Masukkan fungsi yang telah dibuat pada urls.py agar dapat dipanggil pada main.html

    from main.views import edit_product

Lalu tambahkan url ke urlpatterns dengan cara berikut
        
    path('edit-product/<int:id>', edit_product, name='edit_product'),

Panggil dan buat button edit_product yang telah dibuat ke main.html dengan kode 

    <a href="{% url 'main:edit_product' product.id %}">
                        <button>Edit</button>
                    </a>


- [x] Kustomisasi halaman login, register, add product, edit product semenarik mungkin.

    saya memanfaatkan inline CSS dengan menyertakan elemen <style> di bagian atas HTML. Saya memilih inline CSS karena menurut saya ini adalah opsi yang lebih sederhana dan sesuai untuk pemula dalam mengatur dan menggunakannya.


## Tugas 6
>1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

- [x] synchronous programming: 
   
   model pemrograman di mana tugas-tugas dieksekusi satu per satu secara berurutan. Dalam model ini, setiap tugas harus menunggu tugas sebelumnya selesai sebelum dapat dimulai. Ini berarti bahwa eksekusi program terblokir sampai setiap tugas selesai. Synchronous programming sederhana dan mudah dipahami, tetapi dapat menyebabkan ketidakefisienan dan penundaan jika tugas-tugas membutuhkan waktu lama untuk selesai.  
    
- [x] asynchronous programming: 

    model pemrograman di mana tugas-tugas dapat dieksekusi secara independen dan konkuren. Dalam model ini, tugas-tugas dapat dimulai dan dieksekusi secara paralel, tanpa harus menunggu tugas sebelumnya selesai. Asynchronous programming memungkinkan eksekusi non-blocking, yang berarti program dapat terus menjalankan tugas-tugas lain sambil menunggu beberapa tugas tertentu selesai. Hal ini dapat meningkatkan kinerja dan responsivitas keseluruhan program, terutama dalam situasi di mana tugas-tugas melibatkan menunggu sumber daya eksternal atau melakukan operasi yang memakan waktu.  
    
Perbedaan utama antara asynchronous dan synchronous programming terletak pada bagaimana tugas-tugas dieksekusi dan bagaimana program mengelola alur eksekusi. Dalam synchronous programming, tugas-tugas dieksekusi satu per satu secara berurutan, sedangkan dalam asynchronous programming, tugas-tugas dapat dieksekusi secara independen dan konkuren. Asynchronous programming memungkinkan eksekusi non-blocking, yang dapat meningkatkan kinerja dan responsivitas, terutama dalam situasi di mana tugas-tugas melibatkan menunggu sumber daya eksternal atau melakukan operasi yang memakan waktu.


>2 .Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Paradigma event-driven programming adalah pendekatan pemrograman di mana program merespons kejadian atau peristiwa yang terjadi secara asinkron. Ini berarti program akan menjalankan tugas tertentu hanya ketika suatu peristiwa atau kejadian yang telah ditentukan terjadi, tanpa harus secara aktif menunggu atau mengawasi perubahan. Paradigma ini sangat umum dalam pemrograman web, khususnya saat menggunakan JavaScript dan AJAX.

- [x] Contoh penerapannya:

Pada Html, diberikan program script untuk add product

        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)
            document.getElementById("form").reset()
            return false
        }

>3. Jelaskan penerapan asynchronous programming pada AJAX.

Asynchronous programming pada AJAX adalah cara di mana aplikasi web dapat berkomunikasi dengan server tanpa harus menunggu atau menghentikan segalanya. Ini membuat aplikasi web tetap responsif dan efisien. Pada dasarnya, kita mengirimkan permintaan ke server dan memberikan instruksi tentang apa yang harus dilakukan ketika respons dari server sudah siap. Contoh sederhana adalah mengambil data dari server dan menampilkannya di halaman web tanpa mengganggu pengalaman pengguna.

>4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.

Penerapan AJAX menggunakan Fetch API dan library jQuery adalah dua pendekatan yang berbeda dalam mengelola permintaan asynchron di aplikasi web. Berikut perbedaanya berdasarkan beberapa faktor:

1. **Kemudahan Penggunaan**:
- **Fetch API**: Lebih baru dan sederhana dalam sintaksis.
- **jQuery**: Lebih lengkap tetapi mungkin terasa lebih berat jika hanya digunakan untuk AJAX.

2. **Ukuran File**:
- **Fetch API**: Lebih kecil karena merupakan bagian dari JavaScript modern.
- **jQuery**: Lebih besar karena merupakan library terpisah.

3. **Kompatibilitas**:
- **Fetch API**: Dukungan untuk browser modern, mungkin memerlukan dukungan tambahan untuk browser lama.
- **jQuery**: Mendukung banyak browser, termasuk yang lama.

4. **Ekosistem dan Dokumentasi**:
- **Fetch API**: Banyak tutorial dan dokumentasi, tetapi mungkin tidak sebanyak jQuery.
- **jQuery**: Ekosistem dan dokumentasi yang kuat, terutama bagi pemula.

5. **Performa**:
- **Fetch API**: Cenderung lebih cepat dan efisien dalam penggunaan sumber daya.
- **jQuery**: Memiliki fitur-fitur bagus, namun dalam beberapa situasi, Fetch API bisa lebih cepat karena lebih ringan.

   Pilihan antara Fetch API dan jQuery untuk AJAX tergantung pada kebutuhan. Menurut pendapat saya, jika ingin menggunakan pendekatan yang lebih modern, lebih ringan, dan tidak tergantung pada library eksternal, maka Fetch API adalah pilihan yang baik. 

>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

- [x] Mengubah tugas 5 yang telah dibuat sebelumnya menjadi menggunakan AJAX.

Ubahlah kode tabel data item agar dapat mendukung AJAX GET. Untuk mengubah kode tabel menjadi tabel pertama tama kita harus membuat fungsi pada main.html untuk memanggil tabel, dengan mengubah html tabel menjadi kode berikut ini

        <table id="product_table"></table>

Lakukan pengambilan task menggunakan AJAX GET. Buat Fungsi pada views.py untuk membuat fungsi mengambil get product

    @login_required(login_url='/login')
    def get_product_json(request):
        product_item = Product.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', product_item))

Selanjutnya setelah membuat fungsi pada views.py, buat routing pada urls.py, import get product json agar bisa di tambahkan, selanjutnya agar bisa dipanggil pada html, tambahkan urlspath dengan kode berikut

        path('get-product/', get_product_json, name='get_product_json'),

Setelah menambahkan urls.py, buat javascript dengan menambahkan <script> oada main.html dengan menambahkan kode:

        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }

- [x] AJAX POST

Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item. Untuk membuat tombol membuka modal form untuk menambahkan item menambahkannya pada navbar, dengan memanggil:

        <a class="nav-link" type="button"  data-bs-target="#exampleModal" data-bs-toggle="modal" style="color: #4162FF; font-weight: 600; padding-right: 20px;" >Make Product by Ajax</a>


Dengan kode modal pada html untuk membuat modal yang nantinya berguna untuk add product:

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="category" class="col-form-label">Category:</label>
                                <input type="text" class="form-control" id="category" name="category"></input>
                            </div>
                            <div class="mb-3">
                                <label for="price" class="col-form-label">Price:</label>
                                <input type="number" class="form-control" id="price" name="price"></input>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                    </div>
                </div>
            </div>


 Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data. Pada file views.py import @crsf_exempt dan menambahkan fungsi add product ajax pada code:

    @csrf_exempt
    def add_product_ajax(request):
        if request.method == 'POST':
            name = request.POST.get("name")
            artist = request.POST.get("artist")
            price = request.POST.get("price")
            description = request.POST.get("description")
            image_url = request.POST.get("image_url")
            detail = request.POST.get("detail")
            user = request.user
            new_product = Product(name=name,artist = artist, price=price, description=description, user=user, image_url = image_url, detail=detail )
            new_product.save()

            return HttpResponse(b"CREATED", status=201)

        return HttpResponseNotFound()

Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat. Setelah menambahkan fungi add_product_ajax pada path, dengan cara membuka urls.py setelah itu mengimpor add_product_ajax dan menambahkan urlpatterns dengan code:

        path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),

Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/. Untuk menghubungkan form dengan path create-ajax buat function addProduct kedalam kode <script>, berikut merupakan kodenya:

    function addProduct() {
        fetch("{% url 'main:add_product_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshProducts).then(refreshCard)

        document.getElementById("form").reset()
        return false
    }

    document.getElementById("button_add").onclick = addProduct


- [x] Melakukan add-commit-push ke GitHub