@echo off
setlocal
cd /d "%~dp0"

where npm >nul 2>nul
if errorlevel 1 (
    echo Node.js and npm are required. Install Node.js 20.19 or newer, then try again.
    pause
    exit /b 1
)

echo Starting Astra Chess and Arcade. Keep this window open while you play.
call npm run dev -- --host 127.0.0.1 --open /chess-arcade/
pause
