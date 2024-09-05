import socket
from Crypto.Cipher import AES
import os

# Configuration
SERVER_HOST = '10.78.18.113'  # Replace with your server's IP
SERVER_PORT = 12345        # Port number to connect to
KEY = b'your16bytekey123'  # Must match the server key

# Setup the AES cipher
cipher = AES.new(KEY, AES.MODE_EAX)

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Send encrypted data
message = b"Hello from the VPN client!"
nonce = os.urandom(16)
cipher = AES.new(KEY, AES.MODE_EAX, nonce)
encrypted_message = nonce + cipher.encrypt(message)
client_socket.sendall(encrypted_message)

# Receive an encrypted response
encrypted_response = client_socket.recv(1024)

# Decrypt the response
nonce = encrypted_response[:16]
ciphertext = encrypted_response[16:]
cipher = AES.new(KEY, AES.MODE_EAX, nonce)
plaintext = cipher.decrypt(ciphertext)

print(f"Received data (decrypted): {plaintext.decode('utf-8')}")

client_socket.close()