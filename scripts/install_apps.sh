#!/bin/bash
# Lune Linux - Setup Dependencies & Educational Apps

echo "Mulai menginstal dependensi Lune Linux..."

# Update sistem
sudo apt-get update && sudo apt-get upgrade -y

# Install aplikasi utilitas dan dock (Plank)
sudo apt-get install -y plank xfce4-appfinder git wget curl ttf-mscorefonts-installer

# Download dan Install WPS Office
wget -O wps-office.deb https://wdl1.pcfg.cache.wpscdn.com/wpsdl/wpsoffice/download/linux/11719/wps-office_11.1.0.11719.XA_amd64.deb
sudo dpkg -i wps-office.deb
sudo apt-get install -f -y

echo "Instalasi dependensi selesai!"
