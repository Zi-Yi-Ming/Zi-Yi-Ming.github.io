@echo off
rem ZYM site local preview launcher (double-click or `start scripts\start-preview.cmd`)
cd /d "%~dp0.."
echo ============================================
echo  ZYM preview server
echo  Open: http://localhost:1399/
echo  Close this window to stop the server.
echo ============================================
hugo server --port 1399 --disableLiveReload --quiet
pause
