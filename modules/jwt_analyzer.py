import jwt
import base64
from utils.rich_logger import log_info, log_success

def decode_jwt(token):
    try:
        parts = token.split('.')
        if len(parts) != 3:
            return None

        header = base64.urlsafe_b64decode(parts[0] + '==').decode()
        payload = base64.urlsafe_b64decode(parts[1] + '==').decode()

        return header, payload
    except Exception as e:
        return None

def run(jwt_file="outputs/jwt_tokens.txt"):
    log_info("Analyzing JWT tokens...")
    with open(jwt_file) as f:
        tokens = [line.strip() for line in f if line.strip()]

    with open("outputs/jwt_analysis.txt", "w") as out:
        for token in tokens:
            result = decode_jwt(token)
            if result:
                header, payload = result
                out.write(f"[+] Token: {token}\nHeader: {header}\nPayload: {payload}\n\n")

    log_success("JWT token analysis complete.")

