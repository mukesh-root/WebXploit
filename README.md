# WebXploit

**WebXploit** is a powerful, modular web penetration testing framework designed for modern recon, exploitation, and post-exploitation. It automates key steps in the web security assessment process, from subdomain enumeration to secret leaks, vulnerability scanning, and advanced token analysis.

---

## 🚀 Features

- 🔍 **Subdomain Enumeration** (Sublist3r + Amass)  
- 🌐 **Live Subdomain Filtering** using HTTPX with 403 logging  
- 🕵️‍♂️ **Parameter Discovery** using ParamSpider  
- 💉 **SQL Injection Detection** using SQLMap  
- 📁 **Directory Bruteforcing** with support for custom wordlists  
- 🔐 **Secret Leak Detection** from JavaScript files & responses  
- 🛡️ **WAF Bypass Detection** with smart payloads  
- 📊 **Vulnerability Scanning** using Nuclei  
- 🧠 **JWT Token Analyzer**  
- ⚠️ **Subdomain Takeover Detection**  
- 🎯 **Post-Exploitation Module Support**  
- 💻 **Rich Terminal Output** with `rich`  
- ⚙️ **Multiprocessing** for speed (Dirbuster & Nuclei)  
- 📝 **HTML/Markdown Report Generation**  
- 🔄 **Mode Switching**: Recon / Exploitation / Post-Exploitation  

---

## 📦 Installation

> One-liner install:
```bash
curl -sL https://raw.githubusercontent.com/mukesh-root/WebXploit/main/install.sh | bash
```

Manual installation:
```bash
git clone https://github.com/mukesh-root/WebXploit.git
cd WebXploit
pip install -r requirements.txt
```

---

## 🛠️ Usage

```bash
python3 webxploit.py --target example.com --mode full
```

Available Modes:
- `--mode recon`: Only subdomain, parameters, JS analysis
- `--mode exploit`: SQLMap, Dirbuster, Nuclei, JWT, Secrets
- `--mode post`: Post-exploitation modules
- `--wordlist custom.txt`: Use custom wordlist for directory brute-force

---
Reports are saved in `/reports`:
- `report.html`
- `report.md`

---

## ⚠️ Legal Disclaimer

**This tool is for educational and authorized security testing only.**  
Do not use it against targets without proper permission.

---

## 🙌 Contribution

Pull requests are welcome! Suggest improvements, submit bug fixes, or add your own modules!

---

## 📄 License

MIT License © 2025 [YourName]
