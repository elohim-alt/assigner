@echo off

REM Navigate to the project root
cd %~dp0..

REM Create virtual environment if it doesn't exist
if not exist "venv" (
  python -m venv venv
)

REM Activate virtual environment
venv\Scripts\activate

REM Install requirements
pip install -r requirements.txt

REM Deactivate the virtual environment
deactivate
