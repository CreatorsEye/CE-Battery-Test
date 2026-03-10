@echo off
echo Installing CEBT (Creators Eye Battery Tester) for Windows...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo.
    echo Please install Python 3.6 or higher from:
    echo https://www.python.org/downloads/
    echo.
    echo After installing Python, run this installer again.
    echo.
    echo Or use the HTML GUI version instead:
    echo https://github.com/CreatorsEye/battery-reporter/tree/main/GUI/HTML
    pause
    exit /b 1
)

REM Create installation folder
if not exist "%USERPROFILE%\CEBT" mkdir "%USERPROFILE%\CEBT"
copy cebt.py "%USERPROFILE%\CEBT\" /Y >nul

REM Create batch wrapper in system PATH
echo @echo off > "%WINDIR%\cebt.bat"
echo python "%USERPROFILE%\CEBT\cebt.py" %%* >> "%WINDIR%\cebt.bat"

echo ✅ CEBT installed successfully!
echo.
echo You can now use 'cebt' from any terminal:
echo   cebt /S    - Start test
echo   cebt /R    - Show results
echo   cebt /C    - Compare tests
echo   cebt /L    - Open last report
echo   cebt /O    - Set output folder
echo   cebt /H    - Show help
echo.
pause
