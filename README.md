<p align="center">
  <img src="assets/logo/lune-logo-color-512.png" width="120" alt="Logo Lune Linux">
</p>

<h1 align="center">Lune Linux</h1>

<p align="center">
  <em>Distro Linux berbasis Ubuntu dengan tampilan dan pengalaman yang terinspirasi macOS:<br>
  dock dengan efek zoom, panel atas transparan, animasi halus, dan Dynamic Island.</em>
</p>

> **Status: pra-rilis (0.1).** ISO sudah bisa dibangun dan diinstal di VirtualBox, tetapi
> belum stabil dan **belum dites di perangkat keras asli**. Jangan dipakai sebagai satu-satunya
> sistem tanpa backup. Lihat [Masalah yang diketahui](#masalah-yang-diketahui).

Lune Linux adalah *remix* Ubuntu: kernel, paket, dan installer-nya milik Ubuntu. Yang dibuat
Lune adalah kustomisasi desktop dan skrip untuk membangun ISO-nya.

## Fitur

- **Dock di bawah** dengan efek membesar saat kursor di atas ikon ([MacOS Dock](https://extensions.gnome.org/extension/10719/macos-dock/))
- **Panel atas transparan** dengan blur ([Blur my Shell](https://extensions.gnome.org/extension/3193/blur-my-shell/))
- **Tema WhiteSur**: GTK, GNOME Shell, ikon, kursor, dan font **Inter**; tombol jendela di kiri
- **Dynamic Island** buatan sendiri: notifikasi, kontrol media, jam, dan (opsional) asisten AI lokal
- **Wallpaper dan logo original** (bulan sabit), tersedia versi gelap dan terang

## Mulai cepat

Belum ada rilis ISO publik. Ada dua jalan:

1. **Bangun ISO sendiri**: ikuti [docs/BUILD-ISO.md](docs/BUILD-ISO.md).
2. **Cuma mau tampilannya di Ubuntu yang sudah ada** (tanpa membuat ISO), jalankan dari folder repo ini:

   ```bash
   bash scripts/01-setup-tools.sh
   bash scripts/02-apply-theme.sh      # lalu log out dan login lagi
   bash scripts/03-extensions.sh       # lalu log out dan login lagi
   ```

   Coba di VM dulu supaya desktop utama aman kalau ada yang berantakan.

## Dokumentasi

| Dokumen | Isi |
|---------|-----|
| [docs/USER-MANUAL.md](docs/USER-MANUAL.md) | **Manual pengguna**: instalasi, desktop, Dynamic Island, kustomisasi |
| [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Masalah yang pernah ditemui dan cara mengatasinya |
| [docs/BUILD-ISO.md](docs/BUILD-ISO.md) | Cara membangun ISO dengan Cubic, langkah demi langkah |
| [docs/ROADMAP.md](docs/ROADMAP.md) | Rencana pengembangan |
| [CHANGELOG.md](CHANGELOG.md) | Riwayat perubahan |
| [THIRD-PARTY.md](THIRD-PARTY.md) | Komponen pihak ketiga dan lisensinya |

## Struktur repo

```
lune-linux/
├── README.md
├── LICENSE
├── THIRD-PARTY.md
├── CHANGELOG.md
├── assets/
│   ├── logo/               <- logo bulan sabit (SVG putih, SVG warna, PNG)
│   ├── wallpapers/         <- wallpaper night dan dawn (JPG 3840x2160 + sumber SVG)
│   └── source/             <- skrip pembuat logo dan wallpaper
├── docs/                   <- manual, troubleshooting, build ISO, roadmap
├── scripts/
│   ├── 01-setup-tools.sh   <- pasang tool dasar
│   ├── 02-apply-theme.sh   <- tema WhiteSur, ikon, kursor, font
│   ├── 03-extensions.sh    <- dock, blur, panel
│   └── 10-stage-overlay.sh <- kumpulkan ekstensi untuk dimasukkan ke ISO
└── iso/
    ├── chroot-customize.sh <- dijalankan di dalam Cubic (tema, default, branding)
    └── overlay/            <- file yang disalin ke sistem ISO (wallpaper, ekstensi)
```

## Masalah yang diketahui

Ini kondisi build 0.1. Beberapa sudah ada perbaikan di skrip yang **belum dibuktikan** di ISO baru.

- **Dock bawaan Ubuntu masih muncul di sisi kiri** pada build 0.1. Skrip sekarang mematikannya otomatis
  (`disabled-extensions`), tetapi belum dites di ISO baru. Cara manual ada di [manual pengguna](docs/USER-MANUAL.md#mematikan-dock-bawaan-ubuntu).
- **Wallpaper default Lune belum terterapkan** pada build 0.1 (masih wallpaper Ubuntu). Penyebabnya
  sedang diselidiki, lihat [troubleshooting](docs/TROUBLESHOOTING.md#wallpaper-lune-tidak-menjadi-default).
- **Branding Ubuntu masih tersisa**: ikon di pojok kiri atas panel, installer, dan layar boot.
- **AI dan suara di Dynamic Island tidak ikut ISO** (butuh Ollama dan model yang besar); dipasang setelah instalasi.
- Sekali terlihat: `systemd-journald` crash saat instalasi di VirtualBox. Instalasi tetap selesai;
  belum diketahui apakah ini bug Ubuntu 26.04, VirtualBox, atau kustomisasi Lune.

## Catatan hukum

Lune Linux **tidak berafiliasi** dengan Apple maupun Canonical. Tampilannya *terinspirasi* macOS, tetapi
tidak memakai aset, logo, ataupun nama Apple. Lune adalah turunan Ubuntu ("based on Ubuntu"); jangan
memakai nama atau logo Ubuntu sebagai nama distro, dan periksa kebijakan merek dagang Canonical
sebelum membagikan ISO ke publik. Rincian lisensi komponen ada di [THIRD-PARTY.md](THIRD-PARTY.md).

Skrip dan dokumentasi di repo ini berlisensi [MIT](LICENSE).
