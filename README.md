# WebXploit 🔍

**WebXploit** is a powerful and sophisticated web exploitation framework that automates reconnaissance, vulnerability scanning, and post-exploitation analysis. Designed for ethical hackers and security researchers, it brings together some of the most potent tools into a single orchestrated engine.

---

## ✨ Features

- 🔎 **Subdomain Enumeration** using Sublist3r and Amass
- ✅ **Live Subdomain Filtering** with 403 response logging (via httpx)
- ⛏️ **Parameter Discovery** via ParamSpider
- ⚡ **SQL Injection Testing** using SQLMap
- 📚 **Directory Fuzzing** using Dirsearch (supports custom wordlists)
- 🔍 **Nuclei Vulnerability Scanning** (parallelized)
- 🔐 **Secret Leak Detection** from JavaScript and HTTP responses
- 🔹 **JWT Analyzer**
- 📡 **Subdomain Takeover Detection**
- 📉 **HTML/Markdown Reporting**
- ⚖️ **Modular Execution Modes**: `recon`, `post`, `full`

---

## ⚡ Installation

### Option 1: Manual Setup

#### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/WebXploit.git
cd WebXploit
```

#### 2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

#### 3. Install required external tools:
```bash
sudo apt update && sudo apt install amass sqlmap httpx nuclei -y
pip install sublist3r paramspider
```

### Option 2: Dockerized Setup

#### 1. Build the Docker image:
```bash
docker build -t webxploit .
```

#### 2. Run WebXploit:
```bash
docker run -v $PWD/outputs:/app/outputs webxploit --target example.com --mode full
```

---

## 🔧 Usage

### Basic Command:
```bash
python3 webxploit.py --target example.com --mode full
```

### Use Custom Wordlist for Dir Fuzzing:
```bash
python3 webxploit.py --target example.com --dir-wordlist wordlists/custom.txt
```

### Show Help:
```bash
python3 webxploit.py --help
```

---

## 📃 Output Structure

- `outputs/`: Raw `.txt` outputs from each module
- `reports/`: Auto-generated HTML and Markdown reports

---
> ⚠️ **Always ensure you have permission to test a target.**

---

## 🌊 Contributing
Pull requests are welcome! Please make sure to update tests as appropriate and follow the contribution guidelines.

---

## 👁️ License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 🎉 Get Started Now
Your ultimate recon-to-exploitation pipeline is just a command away:
```bash
python3 webxploit.py --target vulnerable-web.com --mode full --waf-bypass
```

> Stay ethical. Stay sharp. Hack responsibly ⚡

