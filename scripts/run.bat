@echo off

if "%~2" == "" (
  echo Usage: scripts\setup_and_run.bat ^<shipments_file^> ^<drivers_file^>
  exit /b 1
)

REM Navigate to the project root
cd %~dp0..

REM Activate virtual environment
venv\Scripts\activate

REM Run the assignment optimizer
python -m assigner %1 %2

REM Deactivate the virtual environment
deactivate
