source venv/bin/activate

apt-get install libjpeg-progs optipng
pip install -r requirements.txt

pelican-themes --install theme_born2data/
pelican-themes -l

