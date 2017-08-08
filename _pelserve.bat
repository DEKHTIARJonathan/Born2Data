%~d1
cd "%~p1"
call venv\Scripts\activate.bat

cd "./docs"
python -m pelican.server
popd

PAUSE;