import shutil
from utils.rich_logger import log_info, log_error

REQUIRED_TOOLS = {
    "sublist3r": "https://github.com/aboul3la/Sublist3r",
    "amass": "https://github.com/owasp-amass/amass",
    "httpx": "https://github.com/projectdiscovery/httpx",
    "nuclei": "https://github.com/projectdiscovery/nuclei",
    "paramspider": "https://github.com/devanshbatham/ParamSpider",
    "sqlmap": "https://github.com/sqlmapproject/sqlmap"
}

def check_tools():
    log_info("[*] Checking for required external tools...")
    missing = False

    for tool, url in REQUIRED_TOOLS.items():
        if shutil.which(tool) is None:
            log_error(f"[-] {tool} not found. Install it from {url}")
            missing = True
        else:
            log_info(f"[+] {tool} is available.")

    if not missing:
        log_info("[+] All required tools are installed.")
    else:
        log_error("[-] One or more required tools are missing. Please install them before proceeding.")
