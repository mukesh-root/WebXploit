import argparse
from core_engine import run_mode
from utils.rich_logger import log_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WebXploit - Advanced Web Exploitation Toolkit")
    parser.add_argument("-t", "--target", help="Target domain", required=True)
    parser.add_argument("-w", "--wordlist", help="Custom wordlist for DirBuster", required=False)
    args = parser.parse_args()

    log_info(f"Starting WebXploit for target: {args.target}")
    run_mode(args.target, args.wordlist)
