import subprocess
from multiprocessing import Pool
from utils.rich_logger import log_info, log_success

def run(subdomain_file, wordlist=None):
    with open(subdomain_file) as f:
        targets = [line.strip() for line in f if line.strip()]

    wordlist = wordlist or "common.txt"
    pool = Pool(processes=5)
    pool.starmap(scan_target, [(target, wordlist) for target in targets])
    pool.close()
    pool.join()
    log_success("Directory brute-force complete.")

def scan_target(domain, wordlist):
    log_info(f"Dirbusting: {domain}")
    output = subprocess.getoutput(f"dirsearch -u http://{domain} -e php,html,js -w {wordlist}")
    with open("outputs/dirbuster_results.txt", "a") as f:
        f.write(f"\n[+] {domain}\n{output}\n")
