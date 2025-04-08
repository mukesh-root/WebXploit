import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.tool_check import check_tools
from modules.subdomain_enum import run as run_subdomain_enum, filter_live_subdomains
from modules.param_discovery import run as run_param_discovery
from modules.js_secrets import run as run_js_secrets
from modules.sql_injector import run as run_sqlmap
from modules.dir_fuzz import run as run_dirb
from modules.nuclei_scan import run as run_nuclei
from modules.jwt_analyzer import run as run_jwt
from modules.subdomain_takeover import run as run_subtake
from modules.post_exploit import run as run_post
from utils.rich_logger import log_info, log_error

def run_recon(target):
    log_info("[RECON] Starting subdomain enumeration...")
    run_subdomain_enum(target)

    log_info("[RECON] Filtering live subdomains...")
    filter_live_subdomains()

    log_info("[RECON] Starting parameter discovery...")
    run_param_discovery(target)

    log_info("[RECON] Detecting JS secrets...")
    run_js_secrets(target)

def run_exploit(target):
    log_info("[EXPLOIT] Running SQLMap on parameterized URLs...")
    run_sqlmap(target)

    log_info("[EXPLOIT] Starting directory brute-force...")
    run_dirb(target)

    log_info("[EXPLOIT] Running Nuclei scan...")
    run_nuclei(target)

    log_info("[EXPLOIT] Analyzing JWT tokens...")
    run_jwt(target)

    log_info("[EXPLOIT] Checking for subdomain takeover...")
    run_subtake(target)

def run_post_exploit(target):
    log_info("[POST] Running post-exploitation module...")
    run_post(target)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="WebXploit - Web Pentest Automation Toolkit")
    parser.add_argument("mode", choices=["recon", "exploit", "post", "full"], help="Mode to run")
    parser.add_argument("target", help="Target domain")
    args = parser.parse_args()

    check_tools()

    if args.mode == "recon":
        run_recon(args.target)
    elif args.mode == "exploit":
        run_exploit(args.target)
    elif args.mode == "post":
        run_post_exploit(args.target)
    elif args.mode == "full":
        run_recon(args.target)
        run_exploit(args.target)
        run_post_exploit(args.target)
    else:
        log_error("Invalid mode selected.")
