@echo off
setlocal

echo.
echo [1/4] Starting OWASP ZAP using zap.exe on port 8081...
start "" "C:\Program Files\ZAP\Zed Attack Proxy\zap.exe" -daemon -port 8081 -config api.disablekey=true

echo.
echo [2/4] Waiting for ZAP to become available...
timeout /t 20 /nobreak >nul

echo.
echo [3/4] Running zap_scan.py script...
python zap_scan.py

echo.
echo [4/4] Shutting down ZAP...
curl http://127.0.0.1:8081/JSON/core/action/shutdown/

echo.
echo Done. Check zap_report.html for results.
pause
endlocal
