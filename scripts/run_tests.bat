@echo off

REM Navigate to the project root
cd %~dp0..

REM Activate virtual environment
venv\Scripts\activate

REM Run tests using pytest (assuming it's already installed)
pytest

REM Deactivate the virtual environment
deactivate
