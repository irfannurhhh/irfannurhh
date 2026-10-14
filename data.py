# ===== EDIT ISI WEBSITE DI SINI =====
# Gambar: taruh di static/img/..., tulis path relatif dari folder static.
NAV = [("about", "Tentang"), ("organisasi", "Organisasi"), ("magang", "Magang"), ("sertifikat", "Sertifikat"),
       ("skills", "Skills"), ("album", "Album"), ("projects", "Project"), ("contact", "Kontak")]

P = dict(name="Irfan Nur Hidayat", role="Mahasiswa", major="Teknologi Rekayasa Otomasi",
         univ="Universitas Diponegoro (UNDIP)", photo="img/profile.jpg",
         tagline="Mahasiswa yang bersemangat membangun solusi otomasi, dari sensor dan mikrokontroler sampai aplikasi web.")

ABOUT = dict(
    text=["Saya merupakan mahasiswa Teknologi Rekayasa Otomasi Universitas Diponegoro yang memiliki ketertarikan pada teknologi, elektronika, pemrograman, dan sistem otomasi. Ketertarikan tersebut saya kembangkan melalui kegiatan praktikum elektronika, pemrograman Python, serta proyek pengendalian tiga LED berbasis ESP32 menggunakan web server.

Saya memiliki kemauan untuk terus belajar, bertanggung jawab, dan mampu bekerja sama dalam tim. Melalui pengalaman praktikum dan proyek yang telah dikerjakan, saya terus mengembangkan kemampuan teknis, pemecahan masalah, serta kesiapan untuk menghadapi tantangan di dunia profesional."],
    education=[dict(school="Universitas Diponegoro", detail="D4 Teknologi Rekayasa Otomasi", year="2026 – sekarang")],
    interests=["Engineering", "Programming", "Automation", "Teknologi"],
    goals="Berkarier sebagai engineer otomasi dan terus belajar teknologi industri 4.0.")

ORGS = [
    dict(name="OSIS SMK Karya Teknologi Jatilawang", role="Sekretaris", period="2023 – 2025",
        desc="Mengelola kegiatan dan administrasi organisasi, mengarsip seluruh dokumen organisasi.", contrib="Menjadi sekretaris utama di event classmeet", photo="img/orgs/org1.jpg"),
    dict(name="PMR WIRA Katana SMK Karya Teknologi Jatilawang", role="Anggota Divisi PDD", period="2024 – 2025",
        desc="Mendokumentasikan seluruh kegiatan, mengelola sosial media organisasi, dan mengarsip seluruh dokumentasi organisasi.", contrib="Mengikuti kegiatan Jumpa Bakti Gembira (JUMBARA) di Desa Sumbang, Banyumas", photo="img/orgs/org2.jpg")
]
        

INTERNS = [dict(company="PT Mada Wikri Tunggal", position="HRD", period="Okt 2024 – Apr 2025",
                desc="Membantu HRD dalam mengelola administrasi karyawan.", tasks=["Mengelola dan merekap absensi karyawan", "Mengelola data karyawan", " Membantu proses tutup buku bulanan"], skills=["Microsoft Excel", "Microsoft Word", "Teamwork"],
                photo="img/magang/magang1.jpg")]

CERTS = [dict(name="Sertifikasi Kompetensi BNSP", org="Badan Nasional Sertifikasi Profesional", year="2026", note="Telah kompeten pada bidang Perawatan dan Perbaikan Otomotif Kendaraan Ringan Roda 4", img="img/certs/cert1.jpg")]

# level hanya indikator visual (0-100), ubah sesukanya
SOFT = [("Communication", 74), ("Teamwork", 76), ("Leadership", 72), ("Problem Solving", 73),
        ("Time Management", 74), ("Adaptability", 75), ("Creativity", 75), ("Responsibility", 74)]

HARD = [("Programming", [("🐍", "Python")]),
        ("Automotive & Mechanical", [("🔧", "Maintenance Light Vehicle"), ("🛠️", "Maintenance Electrical System")]),
        ("Software & Tools", [("💻", "VS Code"), ("🐙", "Git/GitHub"), ("📄", "Microsoft Office")])]

ALBUMS = [dict(slug="kuliah", name="Kegiatan Kuliah"), dict(slug="praktikum", name="Praktikum"),
          dict(slug="organisasi", name="Organisasi"), dict(slug="magang", name="Magang"), dict(slug="pribadi", name="Pribadi")]

PROJECTS = [dict(name="Kontrol LED via Web Server ESP32", img="img/projects/p1.jpg",
                 desc="Mengontrol LED lewat web server lokal di ESP32.", tech=["ESP32", "C++", "HTML"],
                 features=["Kontrol on/off dari browser", "Berjalan di jaringan lokal"], github="", demo="")]

CONTACT = dict(email="irfannurhidayat2020@gmail.com", instagram="https://instagram.com/nrhidyaatt",
               linkedin="https://linkedin.com/in/irfannrhidayat", github="https://github.com/irfannurhhh",
               whatsapp="https://wa.me/6285878918839", location="Semarang, Indonesia")
