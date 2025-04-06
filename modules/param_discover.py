import subprocess
from utils.rich_logger import log_info, log_success

def run(target):
    log_info("Running ParamSpider...")
    cmd = f"python3 ParamSpider/paramspider.py -d {target} -o outputs/parameters.txt"
    subprocess.call(cmd, shell=True)
    log_success("Parameter discovery complete.")

