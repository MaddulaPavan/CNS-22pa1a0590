import hmac
import hashlib

def generate_mac(message, key):
    key = key.encode('utf-8')
    message = message.encode('utf-8')
    mac = hmac.new(key, message, hashlib.sha256).hexdigest()
    return mac

def verify_mac(message, key, received_mac):
    calculated_mac = generate_mac(message, key)
    return calculated_mac == received_mac  

secret_key = "mysecretkey"
message = "Hello, this is a secure message!"
mac = generate_mac(message, secret_key)
print(f"Generated MAC: {mac}")

is_valid = verify_mac(message, secret_key, mac)
print(f"MAC Verification (Original): {is_valid}")

tampered_message = "Hello, this is a tampered message!"
is_valid_tampered = verify_mac(tampered_message, secret_key, mac)
print(f"MAC Verification (Tampered): {is_valid_tampered}")
