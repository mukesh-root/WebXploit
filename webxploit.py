import argparse
import os
from modules import subdomain_enum, param_discover, sqlmap_wrapper, dirbuster, nuclei_scan, secret_leaks, jwt_analyzer, sub_takeover, waf_bypass
from utils.rich_logger import log_info, log_error, log_success


def setup_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="WebXploit: Modular Web Pentest Framework")
    parser.add_argument("--target", required=True, help="Target domain or URL")
    parser.add_argument("--mode", choices=["recon", "exploit", "post", "full"], default="full", help="Mode of operation")
    parser.add_argument("--wordlist", help="Custom wordlist for dirbuster")
    args = parser.parse_args()

    setup_dirs()

    if args.mode in ["recon", "full"]:
        log_info("[RECON] Starting subdomain enumeration...")
        subdomain_enum.run(args.target)

        log_info("[RECON] Filtering live subdomains...")
        subdomain_enum.filter_live_subdomains()

        log_info("[RECON] Starting parameter discovery...")
        param_discover.run(args.target)

        log_info("[RECON] Detecting JS secrets...")
        secret_leaks.run(args.target)

    if args.mode in ["exploit", "full"]:
        log_info("[EXPLOIT] Testing SQL injection with SQLMap...")
        sqlmap_wrapper.run("outputs/parameters.txt")

        log_info("[EXPLOIT] Running directory brute-force...")
        dirbuster.run("outputs/live_subdomains.txt", args.wordlist)

        log_info("[EXPLOIT] Running vulnerability scan using Nuclei...")
        nuclei_scan.run("outputs/live_subdomains.txt")

        log_info("[EXPLOIT] Analyzing JWT tokens...")
        jwt_analyzer.run("outputs/live_subdomains.txt")

        log_info("[EXPLOIT] Detecting subdomain takeovers...")
        sub_takeover.run("outputs/live_subdomains.txt")

    if args.mode in ["post", "full"]:
        log_info("[POST] Executing post-exploitation modules...")
        waf_bypass.run("outputs/live_subdomains.txt")

    log_success("\n🎉 WebXploit scan complete. Check outputs and reports folder for results.")


if __name__ == "__main__":
    main()

