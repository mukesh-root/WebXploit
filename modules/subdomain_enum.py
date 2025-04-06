# modules/subdomain_enum.py

import os
import subprocess
from utils.rich_logger import log_info, log_error

def run(target):
    os.makedirs("outputs", exist_ok=True)

    log_info("[*] Running Sublist3r...")
    subprocess.run(f"sublist3r -d {target} -o outputs/sublist3r.txt", shell=True)

    log_info("[*] Running Amass (passive)...")
    subprocess.run(f"amass enum -d {target} -passive -o outputs/amass.txt", shell=True)

    log_info("[*] Merging subdomains...")
    subprocess.run("cat outputs/sublist3r.txt outputs/amass.txt | sort -u > outputs/final_subdomains.txt", shell=True)

    log_info("[+] Subdomain enumeration complete.")

def filter_live_subdomains():
    if not os.path.exists("outputs/final_subdomains.txt"):
        log_error("final_subdomains.txt not found!")
        return

    try:
        subprocess.run(
            "cat outputs/final_subdomains.txt | httpx -silent -status-code -no-color | tee outputs/httpx_raw.txt | awk '$2 == \"[200]\" || $2 == \"[403]\" {print $1}' > outputs/live_subdomains.txt",
            shell=True,
            check=True,
        )
        log_info("Live subdomains saved to outputs/live_subdomains.txt")
    except subprocess.CalledProcessError:
        log_error("Failed to run httpx for live filtering.")
