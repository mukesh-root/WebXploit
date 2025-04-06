import subprocess
from utils.rich_logger import log_info, log_success

def run(subdomain_file):
    log_info("Checking for subdomain takeover...")
    cmd = f"subzy run --targets {subdomain_file} --hide_fails --output outputs/sub_takeover.txt"
    subprocess.call(cmd, shell=True)
    log_success("Subdomain takeover check complete.")

