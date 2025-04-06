import re
import requests
import os
from utils.rich_logger import log_info, log_success

SECRET_PATTERNS = [
    ("AWS Key", r"AKIA[0-9A-Z]{16}"),
    ("Google API Key", r"AIza[0-9A-Za-z\-_]{35}"),
    ("Slack Token", r"xox[baprs]-([0-9a-zA-Z]{10,48})"),
    ("Private Key", r"-----BEGIN PRIVATE KEY-----"),
    ("Authorization Bearer", r"Bearer [a-zA-Z0-9\-_\.]+"),
]

def run(target):
    log_info("Searching for JS files to analyze...")
    js_urls = get_js_urls(target)
    log_info(f"Found {len(js_urls)} JS files. Scanning for secrets...")

    with open("outputs/secret_leaks.txt", "w") as out:
        for url in js_urls:
            try:
                r = requests.get(url, timeout=5)
                for name, pattern in SECRET_PATTERNS:
                    matches = re.findall(pattern, r.text)
                    for m in matches:
                        out.write(f"[+] {name}: {m} in {url}\n")
            except Exception:
                continue

    log_success("Secret leak analysis complete.")

def get_js_urls(target):
    try:
        r = requests.get(f"http://{target}", timeout=5)
        return re.findall(r'src=["\'](.*?\.js)["\']', r.text)
    except:
        return []
