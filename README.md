# mcroconrollers_curse_work

Приложения раазработано для работы на Debian и Debian подобных системах

### Библиотеки для работы проекта находятся в requirements
pip install -r requirements.txt

### Для работы с text speech
sudo apt-get update

sudo apt-get install mpg321

### После установок для запуска программы запустите

#### в терминале
python3 app.py

#### через IDLE
запускать app.py


### create bash script

1) in HOME DIRECTORY write:
nano start.sh

2) in this file write:

#!/bin/bash

cd mcroconrollers_curse_work/

source .venv/bin/activate

python3 app.py 

while true; do sleep 1000; done

3) save and exit

4) chmod +x start.sh

### auto setup program
#### open terminal
1)   sudo nano /etc/xdg/autostart/display.desktop

2)   in this file(display.desktop) write:

[Desktop Entry]

Name=PiCounter

Exec=/home/nikita/start.sh

3) SAVE FILE

4) sudo reboot

sudo apt-get install build-essential cmake git pkg-config libgtk-3-dev \
libavcodec-dev libavformat-dev libswscale-dev libv4l-dev \
libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev \
gfortran openexr libatlas-base-dev python3-dev python3-numpy \
libtbb2 libtbb-dev libdc1394-22-dev

Сергей Константинович самый лучший преподаватель!!!
