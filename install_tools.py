import os
import shutil
import subprocess

TOOLS = {
    "sublist3r": {
        "check": "sublist3r",
        "install": """
        git clone https://github.com/aboul3la/Sublist3r.git
        cd Sublist3r && pip install -r requirements.txt
        sudo ln -sf $(pwd)/sublist3r.py /usr/local/bin/sublist3r
        chmod +x /usr/local/bin/sublist3r
        """
    },
    "amass": {
        "check": "amass",
        "install": "sudo apt install -y amass"
    },
    "httpx": {
        "check": "httpx",
        "install": "go install github.com/projectdiscovery/httpx/cmd/httpx@latest && sudo cp ~/go/bin/httpx /usr/local/bin"
    },
    "nuclei": {
        "check": "nuclei",
        "install": "curl -s https://api.github.com/repos/projectdiscovery/nuclei/releases/latest | grep 'browser_download_url.*linux-amd64' | cut -d '\"' -f 4 | wget -qi - && chmod +x nuclei-linux-amd64 && sudo mv nuclei-linux-amd64 /usr/local/bin/nuclei"
    },
    "paramspider": {
        "check": "ParamSpider/paramspider.py",
        "install": """
        git clone https://github.com/devanshbatham/ParamSpider.git
        cd ParamSpider && pip install -r requirements.txt
        """
    },
    "sqlmap": {
        "check": "sqlmap",
        "install": "git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev && sudo ln -sf $(pwd)/sqlmap-dev/sqlmap.py /usr/local/bin/sqlmap"
    }
}

def install(tool, command):
    print(f"[*] Installing {tool}...")
    subprocess.call(command, shell=True)

def main():
    for tool, details in TOOLS.items():
        check_cmd = details["check"]
        install_cmd = details["install"]
        found = shutil.which(check_cmd) if '/' not in check_cmd else os.path.exists(check_cmd)
        if found:
            print(f"[+] {tool} is already installed.")
        else:
            print(f"[-] {tool} not found.")
            install(tool, install_cmd)

if __name__ == "__main__":
    main()
