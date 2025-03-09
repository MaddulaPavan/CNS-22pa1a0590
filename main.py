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
