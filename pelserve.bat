%~d1
cd "%~p1"
call venv\Scripts\activate.bat
python -m pelican.server
popd