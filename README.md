# FengYun2 MiniStation
### Your personal station for real time receiving and decoding images from FengYun-2 satellites!
![1](/readme/1.jpg)
## Instalation
clone git:
```
git clone https://github.com/Foxiks/FengYun2_MiniStation.git
cd FengYun2_MiniStation
```
Update all apt packages via command:
```
sudo apt update && sudo apt upgrade
```

Install [GNURadio3.10](https://wiki.gnuradio.org/index.php/InstallingGR) package
```
sudo add-apt-repository ppa:gnuradio/gnuradio-releases
sudo apt-get update
sudo apt-get install gnuradio python3-packaging
```

Install some additional packages via apt:
```
sudo apt-get install libjpeg-dev zlib1g-dev gcc build-essential libffi-dev python3-dev python3-cffi python3-opencv python3-pip git cmake libusb-1.0-0-dev libboost-all-dev gnuradio-dev liblog4cpp5-dev swig gr-osmosdr
```
...and via pip:
```
python3 -m pip install hexhamming construct Pillow psutil
```

Install the GNURadio [gr-Satellites](https://gr-satellites.readthedocs.io/en/latest/installation_intro.html) block extension package:
```
sudo add-apt-repository ppa:daniestevez/gr-satellites
sudo apt-get update
sudo apt-get install gr-satellites
```

Install the GNURadio [gr-FengYun2](https://github.com/Foxiks/gr-FengYun2) block extension package:
```
git clone https://github.com/Foxiks/gr-FengYun2.git
cd gr-FengYun2
mkdir build
cd build
cmake ..
make
sudo make install
sudo ldconfig
```
# Configuration
### Step 1
Compile the demodulator code using the command:
```
grcc FengYun2_Demodulator.grc
```
### Step 2
Change your station settings via:
```
nano settings.json
```
### Step 3 (optional)
Configure the connection to your OrangePi to work remotely via VPN if your station's IP is dynamic.
### Step 4
Adding automatic program launch after booting the Linux system.
1. Create a Systemd Entry ```sudo nano /etc/systemd/system/fengyun2_ministation.service```
   and put:
```
[Unit]
After=network.service
Description=FengYun2 MiniStation
    
[Service]
Type=simple
ExecStart=/home/user/.../FengYun2_MiniStation/fengyun2_ministation.sh
    
[Install]
WantedBy=multi-user.target
```
___Сhange the path to the sh script!___

2. ___Сhange the path to the py3 script in___ ```sudo nano fengyun2_ministation.sh```!
```
#!/bin/bash
#
python3 /home/user/.../FengYun2_MiniStation/FengYun2_MiniStation_Runner.py  /home/user/.../FengYun2_MiniStation/settings.json# <- Change path!
```

3. Set file permission:
```
sudo chmod 744 /home/user/.../FengYun2_MiniStation/fengyun2_ministation.sh
sudo chmod 664 /etc/systemd/system/fengyun2_ministation.service
```

4. Enable Service
```
sudo systemctl daemon-reload
sudo systemctl enable fengyun2_ministation.service
```

5. Start MiniSation!
```
sudo systemctl start fengyun2_ministation.service
```

6. Check Status
```
sudo systemctl status fengyun2_ministation.service
```

### What's next?
So, if you set everything up correctly, then every 28-29 minutes of every hour you will receive several images from the FengYun-2 satellites. They will be saved in the directory specified in the ```settings.json``` file. Now you can make a script to collect these images through your server via SSH and publish them on your website, social networks, etc. Enjoy!
