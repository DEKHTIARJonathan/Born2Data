sudo apt-get install libjpeg-progs optipng libffi-dev nodejs
sudo npm install -g svgo
sudo apt autoremove -y

python -m pip install -U pip
pip install -r requirements.txt

pelican-themes --remove theme_born2data/
pelican-themes --install theme_born2data/
pelican-themes -l
