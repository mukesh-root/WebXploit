# WebXploit

**WebXploit** is a sophisticated, modular web penetration testing framework that automates reconnaissance, vulnerability scanning, exploitation, and post-exploitation tasks with advanced capabilities.

![WebXploit Banner](https://via.placeholder.com/800x200.png?text=WebXploit+by+YourName)

---

## 🚀 Features

- 🔍 **Subdomain Enumeration** (Sublist3r + Amass)  
- 🌐 **Live Filtering** using HTTPX with 403 tracking  
- 🕵️‍♂️ **Parameter Discovery** using ParamSpider  
- 💉 **SQLi Detection** with SQLMap automation  
- 📁 **Directory Bruteforcing** with Dirbuster (custom wordlist supported)  
- 🔐 **Secret Leak Detection** from JS files and HTTP responses  
- 🛡️ **WAF Bypass Payload Testing**  
- 📊 **Nuclei Vulnerability Scanning**  
- 🎯 **JWT Analyzer** for token security inspection  
- ⚠️ **Subdomain Takeover Detection**  
- 🔎 **Post-Exploitation** module support (expandable)  
- 💻 **Rich CLI Output** using `rich`  
- ⚙️ **Multiprocessing** for speed and scalability  
- 📄 **HTML/Markdown Report Generator**  
- 🔄 **Mode Switching**: Recon Mode / Attack Mode / Post-Exploitation  

---

## 📦 Installation

> One-liner (Linux/macOS):
```bash
curl -sL https://raw.githubusercontent.com/<your-username>/WebXploit/main/install.sh | bash
```

Or manually:
```bash
git clone https://github.com/<your-username>/WebXploit.git
cd WebXploit
pip install -r requirements.txt
```

---

## 🛠️ Usage

### Full Attack Chain
```bash
python3 webxploit.py --target example.com --mode full
```

### Recon Only
```bash
python3 webxploit.py --target example.com --mode recon
```

### Post-Exploitation
```bash
python3 webxploit.py --target example.com --mode post
```

### With Custom Wordlist
```bash
python3 webxploit.py --target example.com --wordlist wordlists/custom_dirs.txt
```

---

## 🗂️ Output

All findings are saved to the `outputs/` directory:
- `subdomains.txt`
- `live_subdomains.txt`
- `parameters.txt`
- `dirbuster_output.txt`
- `nuclei_results.txt`
- `secrets_found.txt`
- `jwt_analysis.txt`
- `subdomain_takeovers.txt`

Final summary reports are in `reports/`:
- `report.md`
- `report.html`

## ⚠️ Legal Disclaimer

This tool is intended for **educational purposes only**. Use it only on systems you own or have explicit permission to test. Unauthorized use is illegal and unethical.

---

## ✨ Contributions

Pull requests are welcome! Feel free to improve modules, add detection engines, or enhance report formatting.

---

## 📄 License

MIT License © 2025 YourName
