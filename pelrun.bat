%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pelican content --debug --autoreload  --settings pelicanconf.py
PAUSE;