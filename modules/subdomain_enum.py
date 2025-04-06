import os
import subprocess
from utils.rich_logger import log_info, log_error, log_success

def run(target):
    try:
        log_info("[*] Running Sublist3r...")
        os.system(f"sublist3r -d {target} -o outputs/sublist3r.txt")

        log_info("[*] Running Amass (passive)...")
        os.system(f"amass enum -passive -d {target} -o outputs/amass.txt")

        log_info("[*] Merging subdomains...")
        with open("outputs/sublist3r.txt", "r") as f1, open("outputs/amass.txt", "r") as f2:
            all_subdomains = set(f1.read().splitlines() + f2.read().splitlines())

        with open("outputs/final_subdomains.txt", "w") as fout:
            for sub in sorted(all_subdomains):
                fout.write(sub + "\n")

        log_success("[+] Subdomain enumeration complete. Saved to outputs/final_subdomains.txt")
    except Exception as e:
        log_error(f"Subdomain enumeration failed: {e}")

def filter_live_subdomains():
    if not os.path.exists("outputs/final_subdomains.txt"):
        log_error("outputs/final_subdomains.txt not found!")
        return

    try:
        log_info("[*] Running HTTPX to check for live subdomains (filtering 200 and 403)...")
        os.system(
            'cat outputs/final_subdomains.txt | httpx -silent -status-code -no-color '
            '| tee outputs/httpx_raw.txt '
            '| awk \'$2 == "[200]" || $2 == "[403]" {print $1}\' > outputs/live_subdomains.txt'
        )
        log_success("Live subdomains saved to outputs/live_subdomains.txt")
        log_info("Full HTTPX output saved to outputs/httpx_raw.txt")
    except Exception as e:
        log_error(f"Error during live subdomain filtering: {str(e)}")
