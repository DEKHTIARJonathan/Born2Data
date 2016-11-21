%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install pelican
pip install markdown
pip install Fabric
PAUSE;