import argparse
import os
from modules import (
    subdomain_enum,
    param_discover,
    sqlmap_wrapper,
    dirbuster,
    nuclei_scan,
    secret_leaks,
    jwt_analyzer,
    sub_takeover,
    waf_bypass,
)
from utils.rich_logger import log_info, log_error, log_success


def setup_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="WebXploit: Modular Web Pentest Framework")
    parser.add_argument("--target", "-t", required=True, help="Target domain or URL")
    parser.add_argument("--mode", "-m", choices=["recon", "exploit", "post", "full"], default="full", help="Mode of operation")
    parser.add_argument("--wordlist", "-w", help="Custom wordlist for DirBuster")
    args = parser.parse_args()

    setup_dirs()
    target = args.target

    if args.mode in ["recon", "full"]:
        log_info("[RECON] Starting subdomain enumeration...")
        subdomain_enum.run(target)

        log_info("[RECON] Filtering live subdomains...")
        subdomain_enum.filter_live_subdomains()

        log_info("[RECON] Starting parameter discovery...")
        param_discover.run(target)

        log_info("[RECON] Detecting JS secrets...")
        secret_leaks.run(target)

    if args.mode in ["exploit", "full"]:
        if os.path.exists("outputs/parameters.txt"):
            log_info("[EXPLOIT] Testing SQL injection with SQLMap...")
            sqlmap_wrapper.run("outputs/parameters.txt")
        else:
            log_error("Parameter file not found. Skipping SQLMap.")

        if os.path.exists("outputs/live_subdomains.txt"):
            log_info("[EXPLOIT] Running directory brute-force...")
            dirbuster.run("outputs/live_subdomains.txt", args.wordlist)

            log_info("[EXPLOIT] Running vulnerability scan using Nuclei...")
            nuclei_scan.run("outputs/live_subdomains.txt")

            log_info("[EXPLOIT] Analyzing JWT tokens...")
            jwt_analyzer.run("outputs/live_subdomains.txt")

            log_info("[EXPLOIT] Detecting subdomain takeovers...")
            sub_takeover.run("outputs/live_subdomains.txt")
        else:
            log_error("Live subdomain list not found. Skipping DirBuster, Nuclei, JWT, and Subdomain Takeover modules.")

    if args.mode in ["post", "full"]:
        if os.path.exists("outputs/live_subdomains.txt"):
            log_info("[POST] Executing post-exploitation modules...")
            waf_bypass.run("outputs/live_subdomains.txt")
        else:
            log_error("Live subdomain list not found. Skipping Post-Exploitation.")

    log_success("\n🎉 WebXploit scan complete. Check 'outputs/' and 'reports/' folder for results.")


if __name__ == "__main__":
    main()
