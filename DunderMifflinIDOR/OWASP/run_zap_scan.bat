@echo off
echo Starting OWASP ZAP scan...

start "" "C:\Program Files\ZAP\Zed Attack Proxy\ZAP.exe" -daemon -port 8081 -host 127.0.0.1 -config api.disablekey=true

:: Wait 20 seconds to ensure ZAP finishes booting
timeout /t 20

python zap_scan.py

echo Scan complete. Report saved as zap_report.html.
pause
