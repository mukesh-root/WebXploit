import argparse
from utils.tool_check import check_tools
from modules.subdomain_enum import run as run_subdomain_enum, filter_live_subdomains
from modules.param_discovery import run as run_param_discovery
from modules.js_secrets import run as run_js_secrets
from modules.sql_injection import run as run_sqlmap
from modules.dir_fuzz import run as run_dirbuster
from modules.vuln_scan import run as run_nuclei
from modules.jwt_analysis import run as run_jwt_analysis
from modules.takeover_scan import run as run_takeover
from modules.post_exploitation import run as run_post_exploitation
from utils.rich_logger import log_info, log_error, log_success


def main():
    parser = argparse.ArgumentParser(description="[ WebXploit ] Modular Web Exploitation Framework")
    parser.add_argument("mode", choices=["recon", "exploit", "post", "full"], help="Mode of execution")
    parser.add_argument("target", help="Target domain (e.g. example.com)")
    args = parser.parse_args()

    log_info("[ WebXploit ] Starting execution...")

    check_tools()  # Auto-check and install missing tools

    if args.mode in ["recon", "full"]:
        log_info("[RECON] Starting subdomain enumeration...")
        run_subdomain_enum(args.target)
        filter_live_subdomains()

        log_info("[RECON] Starting parameter discovery...")
        run_param_discovery(args.target)

        log_info("[RECON] Detecting JS secrets...")
        run_js_secrets(args.target)

    if args.mode in ["exploit", "full"]:
        log_info("[EXPLOIT] Starting SQL Injection testing...")
        run_sqlmap(args.target)

        log_info("[EXPLOIT] Starting directory fuzzing...")
        run_dirbuster(args.target)

        log_info("[EXPLOIT] Starting vulnerability scanning with Nuclei...")
        run_nuclei(args.target)

        log_info("[EXPLOIT] Starting JWT analysis...")
        run_jwt_analysis(args.target)

        log_info("[EXPLOIT] Checking for subdomain takeover...")
        run_takeover(args.target)

    if args.mode in ["post", "full"]:
        log_info("[POST] Running post-exploitation modules...")
        run_post_exploitation(args.target)

    log_success("[+] WebXploit execution complete.")


if __name__ == "__main__":
    main()
