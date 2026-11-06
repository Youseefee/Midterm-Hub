@echo off
title Midterm Mastery Hub Launcher
echo ========================================================
echo   Launching Midterm Mastery Hub (منصة مراجعة الميدتيرم)
echo ========================================================
echo.
echo Opening the web application in your default browser...
start "" "%~dp0web\index.html"
echo.
echo Done! If you want to run via a local web server instead,
echo you can run 'python server.py'.
timeout /t 3 >nul
