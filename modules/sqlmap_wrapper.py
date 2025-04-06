import subprocess
import os
from utils.rich_logger import log_info, log_success

def run(param_file):
    if not os.path.exists(param_file):
        log_info("Parameter file not found.")
        return

    with open(param_file) as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        log_info(f"Testing {url} with SQLMap...")
        output = subprocess.getoutput(f"sqlmap -u {url} --batch --output-dir=outputs/sqlmap --level=2")
        with open("outputs/sqlmap_results.txt", "a") as out:
            out.write(f"\n[+] {url}\n{output}\n")

    log_success("SQLMap testing completed.")
