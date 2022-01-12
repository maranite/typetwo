@echo off
rem base is set to this script's parent folder - i.e the workspace folder
set base=%~d0%~p0..\
If NOT EXIST "%base%\.virtualenv\" (
    echo Creating virtual environment
    cd "%base%"
    echo %base%
    python -m venv %base%\.virtualenv\
    %base%\.virtualenv\Scripts\activate.bat
    python -m pip install --upgrade pip
)