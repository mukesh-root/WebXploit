import requests
from utils.rich_logger import log_info, log_success

BYPASS_HEADERS = [
    {"X-Original-URL": "/admin"},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"X-Host": "127.0.0.1"},
    {"X-Forwarded-Host": "127.0.0.1"},
]

def run(urls_file):
    log_info("Testing for WAF bypasses...")
    with open(urls_file) as f:
        urls = [line.strip() for line in f if line.strip()]

    with open("outputs/waf_bypass_results.txt", "w") as out:
        for url in urls:
            for headers in BYPASS_HEADERS:
                try:
                    r = requests.get(url, headers=headers, timeout=5)
                    if r.status_code == 200:
                        out.write(f"[+] Bypass success at {url} with headers {headers}\n")
                        break
                except:
                    continue
    log_success("WAF bypass testing complete.")
