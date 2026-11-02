#!/bin/bash
# Lune Linux - Script Instalasi Tema macOS (WhiteSur)

echo "Mulai menginstall tema macOS (WhiteSur)..."

# Install paket yang dibutuhkan untuk ekstrak dan render tema
sudo apt-get update
sudo apt-get install -y git dialog optipng inkscape libsass1 sassc

# Buat folder sementara untuk proses download
mkdir -p ~/Downloads/lune_temp
cd ~/Downloads/lune_temp

# 1. Unduh dan Install Tema Jendela & Panel (GTK Theme)
echo "Mengunduh Tema Jendela WhiteSur..."
git clone https://github.com/vinceliuice/WhiteSur-gtk-theme.git --depth=1
cd WhiteSur-gtk-theme
./install.sh -t all -N glassy
cd ..

# 2. Unduh dan Install Ikon macOS
echo "Mengunduh Tema Ikon WhiteSur..."
git clone https://github.com/vinceliuice/WhiteSur-icon-theme.git --depth=1
cd WhiteSur-icon-theme
./install.sh -a
cd ..

# Bersihkan folder sementara
rm -rf ~/Downloads/lune_temp

echo "Instalasi tema selesai!"
