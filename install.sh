#!/bin/bash

# WebXploit One-Command Installer

echo -e "\e[94m[+] Starting WebXploit installation...\e[0m"

# System update
sudo apt update -y

# Install system dependencies
sudo apt install -y python3 python3-pip git amass sqlmap httpx nuclei

# Clone the repository
if [ ! -d "WebXploit" ]; then
    git clone https://github.com/<yourusername>/WebXploit.git
fi
cd WebXploit || { echo "Failed to enter WebXploit directory"; exit 1; }

# Install Python dependencies
pip3 install -r requirements.txt

# Install Python-based tools
pip3 install sublist3r paramspider

# Done
echo -e "\e[92m[✔] WebXploit installation completed successfully!\e[0m"
echo -e "\e[93m➡ Run the tool with: python3 webxploit.py --target example.com --mode full\e[0m"
