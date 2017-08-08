%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pip freeze > requirements.txt
PAUSE;