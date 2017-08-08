%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pelican content --settings publishconf.py
pelican content --debug  --settings pelicanconf.py
PAUSE;