from time import sleep
from zapv2 import ZAPv2
import sys

target_url = 'http://localhost:5000/invoices/1001.json'
zap_api_key = ''  # Leave blank unless set
zap = ZAPv2(proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})
print('[*] Waiting for ZAP to become available...')
for attempt in range(30):  # Wait up to 30 seconds
    try:
        zap.core.version  # Ping the ZAP daemon
        print('[+] ZAP is ready.')
        break
    except:
        print(f'    Attempt {attempt + 1}/30: ZAP not ready, retrying...')
        sleep(1)
else:
    print('[!] ZAP did not start in time. Exiting.')
    sys.exit(1)

print(f'[*] Accessing target: {target_url}')
try:
    zap.urlopen(target_url)
except Exception as e:
    print(f'[!] Failed to open target URL: {e}')
    sys.exit(1)

sleep(2)  # Allow passive scan to initialize

print('[*] Starting active scan...')
try:
    scan_id = zap.ascan.scan(target_url)
except Exception as e:
    print(f'[!] Failed to start active scan: {e}')
    sys.exit(1)

while int(zap.ascan.status(scan_id)) < 100:
    print(f"    Scan progress: {zap.ascan.status(scan_id)}%")
    sleep(2)

print('[+] Scan complete. Writing report...')
try:
    with open('zap_report.html', 'w', encoding='utf-8') as f:
        f.write(zap.core.htmlreport())
    print('[+] Report saved as zap_report.html')
except Exception as e:
    print(f'[!] Failed to write report: {e}')
    sys.exit(1)
