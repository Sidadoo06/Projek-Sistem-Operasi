# Changelog

Format mengikuti gaya [Keep a Changelog](https://keepachangelog.com/). Versi pra-rilis.

## [Belum dirilis]

### Ditambahkan
- Dokumentasi: manual pengguna, troubleshooting, panduan build ISO, roadmap.
- Logo bulan sabit dan dua wallpaper original (night dan dawn) di `assets/`.
- Wallpaper Lune ikut tersalin ke ISO lewat `iso/overlay/` dan dipakai otomatis oleh skrip.
- Skrip `chroot-customize.sh` menampilkan `ERROR: gagal di baris ...` kalau ada langkah yang macet.

### Diubah
- `03-extensions.sh` memasang **MacOS Dock** (efek zoom) menggantikan Dash to Dock.
- `chroot-customize.sh` mematikan dock bawaan Ubuntu lewat `disabled-extensions` **(belum dibuktikan di ISO baru)**.

### Diperbaiki
- `chroot-customize.sh` keluar diam-diam di dalam Cubic karena installer WhiteSur memanggil `logname`
  (gagal di chroot). Sekarang `SUDO_USER=root` diatur otomatis.

## [0.1.0] - 2026-11-20 (build pertama, belum stabil)

### Ditambahkan
- ISO pertama dibangun dengan Cubic dari Ubuntu 26.04.1 dan berhasil diinstal di VirtualBox.
- Skrip pemasangan desktop (`scripts/01` sampai `03`) dan staging ekstensi (`scripts/10`).
- Tema WhiteSur, font Inter, ekstensi Blur my Shell, Just Perfection, MacOS Dock, dan Dynamic Island.

### Masalah yang diketahui pada build ini
- Kustomisasi (tema dan ekstensi) belum masuk ke ISO pertama karena bug `logname` di atas; baru terlihat
  pada build berikutnya.
- Dock bawaan Ubuntu masih muncul; wallpaper Lune belum menjadi default; branding Ubuntu masih tersisa.
