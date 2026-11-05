@echo off
setlocal
set "PYTHON_ROADMAP_DIR=%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -Command "$startup = [Environment]::GetFolderPath('Startup'); $shell = New-Object -ComObject WScript.Shell; $shortcut = $shell.CreateShortcut((Join-Path $startup 'Python Field Notes.lnk')); $shortcut.TargetPath = Join-Path $env:PYTHON_ROADMAP_DIR 'start-python-roadmap.bat'; $shortcut.WorkingDirectory = $env:PYTHON_ROADMAP_DIR; $shortcut.WindowStyle = 7; $shortcut.Description = 'Start the local Python Field Notes practice tracker'; $shortcut.Save()"
if errorlevel 1 (
    echo Could not create the Windows Startup shortcut.
    pause
    exit /b 1
)

echo Python Field Notes will start when you sign in to Windows.
echo To disable it, remove "Python Field Notes.lnk" from your personal Startup folder.
pause
