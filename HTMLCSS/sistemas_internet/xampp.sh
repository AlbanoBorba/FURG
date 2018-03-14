wget https://sourceforge.net/projects/xampp/files/XAMPP%20Linux/7.0.15/xampp-linux-x64-7.0.15-0-installer.run/ -O xampp-installer.run
chmod +x xampp-installer.run
sudo ./xampp-installer.run
echo -e '[Desktop Entry]\n Version=1.0\n Name=xampp\n Exec=gksudo /opt/lampp/manager-linux-x64.run\n Icon=/opt/lampp/icons/world1.png\n Type=Application\n Categories=Application' | sudo tee /usr/share/applications/xampp.desktop
# next next next next next finish
sudo apt-get install gksu
#y
