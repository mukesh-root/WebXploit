import subprocess
import os
from utils.rich_logger import log_info, log_success

def run(target):
    log_info("Running Sublist3r...")
    sublist3r_output = subprocess.getoutput(f"sublist3r -d {target} -o outputs/subdomains.txt")
    
    log_info("Running Amass (passive)...")
    amass_output = subprocess.getoutput(f"amass enum -passive -d {target} -o outputs/amass_subs.txt")

    log_info("Merging subdomains...")
    with open("outputs/subdomains.txt", "a") as out:
        with open("outputs/amass_subs.txt") as f:
            for line in f:
                out.write(line)
    
    log_success("Subdomain enumeration complete.")

def filter_live_subdomains():
    import httpx
    log_info("Filtering live subdomains...")
    live = []
    forbidden = []
    with open("outputs/subdomains.txt") as f:
        for line in f:
            url = f"http://{line.strip()}"
            try:
                r = httpx.get(url, timeout=5.0)
                if r.status_code == 403:
                    forbidden.append(line.strip())
                elif r.status_code < 400:
                    live.append(line.strip())
            except:
                continue

    with open("outputs/live_subdomains.txt", "w") as f:
        for l in live:
            f.write(l + "\n")

    with open("outputs/forbidden_subdomains.txt", "w") as f:
        for l in forbidden:
            f.write(l + "\n")

    log_success(f"Live subdomains saved: {len(live)}")
