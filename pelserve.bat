%~d1
cd "%~p1"
call venv\Scripts\activate.bat
pushd "../output"
python -m pelican.server
popd