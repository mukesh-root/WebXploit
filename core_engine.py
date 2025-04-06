
import modules.subdomain_enum as subenum
import modules.param_discover as paramfinder
import modules.sqlmap_wrapper as sqlscanner
import modules.dirbuster as dirbust
import modules.nuclei_scan as nuclei
import modules.secret_leaks as secrets
import modules.jwt_analyzer as jwtanalyze
import modules.sub_takeover as takeover
import modules.waf_bypass as waf
import os

def run_mode(target, wordlist=None):
    if not os.path.exists("outputs"):
        os.makedirs("outputs")

    subenum.run(target)
    secrets.run(target)
    
    # Filter live domains and save 403s
    os.system("httpx -l outputs/subdomains.txt -mc 200,403 -o outputs/live_subdomains.txt -sr -json")

    paramfinder.run(target)
    sqlscanner.run("outputs/parameters.txt")

    dirbust.run("outputs/live_subdomains.txt", wordlist)
    nuclei.run("outputs/live_subdomains.txt")
    waf.run("outputs/live_subdomains.txt")

    takeover.run("outputs/subdomains.txt")
    jwtanalyze.run()

    print("\n[+] WebXploit Scan Completed. Check the outputs/ directory.")
