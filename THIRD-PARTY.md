# Komponen pihak ketiga

Lune Linux memakai dan mendistribusikan komponen milik pihak lain. Daftar ini disusun dari pengetahuan
pembuatnya dan **belum diverifikasi satu per satu**. Sebelum merilis ISO ke publik, buka repositori atau
halaman tiap komponen dan pastikan lisensi serta kewajibannya.

| Komponen | Fungsi di Lune | Lisensi (perkiraan, verifikasi dulu) |
|----------|----------------|--------------------------------------|
| [Ubuntu](https://ubuntu.com) 26.04 | Sistem dasar, kernel, paket, installer | Campuran (GPL dan lain-lain); **merek dagang Canonical** |
| [GNOME](https://www.gnome.org) | Lingkungan desktop | GPL/LGPL |
| [WhiteSur GTK theme](https://github.com/vinceliuice/WhiteSur-gtk-theme) | Tema GTK dan GNOME Shell | GPL-3.0 |
| [WhiteSur icon theme](https://github.com/vinceliuice/WhiteSur-icon-theme) | Ikon | GPL-3.0 |
| [WhiteSur cursors](https://github.com/vinceliuice/WhiteSur-cursors) | Kursor | GPL-3.0 |
| [Inter](https://rsms.me/inter/) | Font sistem | SIL Open Font License 1.1 |
| [Blur my Shell](https://extensions.gnome.org/extension/3193/blur-my-shell/) | Blur panel dan overview | GPL-3.0 |
| [Just Perfection](https://extensions.gnome.org/extension/3843/just-perfection/) | Penyetelan UI Shell | GPL-3.0 |
| [MacOS Dock](https://extensions.gnome.org/extension/10719/macos-dock/) | Dock dengan zoom | **Belum dicek**, lihat repo ekstensinya |
| Dynamic Island (`dynamic-island@claude.local`) | Pill notifikasi, media, jam, AI | Buatan sendiri; tentukan lisensinya |
| Cubic | Alat pembuat ISO (tidak ikut ISO) | Lihat halaman proyek Cubic |

## Catatan merek dagang

- **Ubuntu** dan logonya adalah merek dagang Canonical. Lune adalah turunan Ubuntu; gunakan frasa
  "based on Ubuntu" dan periksa kebijakan merek dagang Canonical sebelum membagikan ISO. Beberapa
  tempat di build 0.1 masih berlogo Ubuntu (ikon panel, installer, layar boot).
- **Apple** dan **macOS** adalah merek dagang Apple Inc. Lune hanya *terinspirasi* gayanya dan tidak memakai
  aset, logo, font, atau nama Apple. Font yang dipakai adalah Inter (bukan font Apple).
- Logo bulan sabit dan wallpaper di `assets/` dibuat khusus untuk Lune Linux.

## Kewajiban GPL

Komponen berlisensi GPL yang didistribusikan dalam ISO mengharuskan penyediaan sumber kodenya. Siapkan
tautan ke sumber (atau salinannya) sebelum membagikan ISO.
