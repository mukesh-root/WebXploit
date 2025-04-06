import subprocess
from multiprocessing import Pool
from utils.rich_logger import log_info, log_success

def run(subdomain_file):
    with open(subdomain_file) as f:
        targets = [line.strip() for line in f if line.strip()]

    pool = Pool(processes=5)
    pool.map(scan_target, targets)
    pool.close()
    pool.join()
    log_success("Nuclei scan complete.")

def scan_target(domain):
    log_info(f"Scanning {domain} with Nuclei...")
    cmd = f"echo {domain} | nuclei -o outputs/nuclei_{domain.replace('.', '_')}.txt"
    subprocess.call(cmd, shell=True)
