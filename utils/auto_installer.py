import os
import platform
import subprocess
import shutil
from utils.rich_logger import log_info, log_error, log_success

REQUIRED_TOOLS = {
    "sublist3r": {
        "url": "https://github.com/aboul3la/Sublist3r",
        "install": [
            "git clone https://github.com/aboul3la/Sublist3r.git",
            "cd Sublist3r && pip install -r requirements.txt",
            "sudo ln -s $(pwd)/sublist3r.py /usr/local/bin/sublist3r"
        ]
    },
    "amass": {
        "url": "https://github.com/owasp-amass/amass",
        "install": [
            "sudo apt install amass -y"
        ]
    },
    "httpx": {
        "url": "https://github.com/projectdiscovery/httpx",
        "install": [
            "go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest",
            "sudo ln -s ~/go/bin/httpx /usr/local/bin/httpx"
        ]
    },
    "nuclei": {
        "url": "https://github.com/projectdiscovery/nuclei",
        "install": [
            "go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest",
            "sudo ln -s ~/go/bin/nuclei /usr/local/bin/nuclei"
        ]
    },
    "sqlmap": {
        "url": "https://github.com/sqlmapproject/sqlmap",
        "install": [
            "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap"
        ]
    },
    "paramspider": {
        "url": "https://github.com/devanshbatham/ParamSpider",
        "install": [
            "git clone https://github.com/devanshbatham/ParamSpider.git"
        ]
    }
}

def run_command(cmd, cwd=None):
    try:
        log_info(f"[RUN] {cmd}")
        subprocess.run(cmd, shell=True, check=True, cwd=cwd)
        return True
    except subprocess.CalledProcessError:
        log_error(f"[FAILED] Command failed: {cmd}")
        return False

def install_tools():
    log_info("[*] Starting tool availability check & auto-install...")

    for tool, meta in REQUIRED_TOOLS.items():
        if shutil.which(tool) is not None:
            log_success(f"[✓] {tool} is already installed.")
            continue

        log_error(f"[✗] {tool} is missing.")
        log_info(f"[*] Attempting to install {tool} from {meta['url']}...")

        for cmd in meta["install"]:
            success = run_command(cmd)
            if not success:
                log_error(f"[-] Failed to install {tool}. Please install it manually from {meta['url']}")
                break
        else:
            log_success(f"[+] {tool} installed successfully!")

    log_info("[*] Auto-installer completed.")
