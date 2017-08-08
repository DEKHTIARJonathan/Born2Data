%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pelican-themes --remove theme_born2data/
pelican-themes --install theme_born2data/
pelican-themes -l
PAUSE;