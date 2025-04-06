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
from utils.rich_logger import log_info, log_success, log_error


def setup_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def run_mode(target, wordlist=None, mode="full"):
    setup_dirs()

    if mode in ["recon", "full"]:
        log_info("[RECON] Running Sublist3r and Amass...")
        subdomain_enum.run(target)

        log_info("[RECON] Filtering live subdomains...")
        subdomain_enum.filter_live_subdomains()

        log_info("[RECON] Finding parameters using ParamSpider...")
        param_discover.run(target)

        log_info("[RECON] Extracting secrets from JS and responses...")
        secret_leaks.run(target)

    if mode in ["exploit", "full"]:
        if os.path.exists("outputs/parameters.txt"):
            log_info("[EXPLOIT] Running SQLMap for SQLi detection...")
            sqlmap_wrapper.run("outputs/parameters.txt")
        else:
            log_error("No parameters.txt found — skipping SQLMap.")

        if os.path.exists("outputs/live_subdomains.txt"):
            log_info("[EXPLOIT] Running DirBuster for directory enumeration...")
            dirbuster.run("outputs/live_subdomains.txt", wordlist)

            log_info("[EXPLOIT] Running Nuclei for vulnerability scanning...")
            nuclei_scan.run("outputs/live_subdomains.txt")

            log_info("[EXPLOIT] Running JWT Analyzer...")
            jwt_analyzer.run("outputs/live_subdomains.txt")

            log_info("[EXPLOIT] Running Subdomain Takeover checks...")
            sub_takeover.run("outputs/live_subdomains.txt")
        else:
            log_error("No live_subdomains.txt found — skipping DirBuster, Nuclei, JWT and SubTakeover.")

    if mode in ["post", "full"]:
        if os.path.exists("outputs/live_subdomains.txt"):
            log_info("[POST] Running WAF Bypass module...")
            waf_bypass.run("outputs/live_subdomains.txt")
        else:
            log_error("No live_subdomains.txt found — skipping WAF Bypass.")

    log_success("\n✅ Scan Complete! Check 'outputs/' and 'reports/' directories.")
