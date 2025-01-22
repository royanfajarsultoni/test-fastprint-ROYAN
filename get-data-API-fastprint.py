import hashlib
from datetime import datetime
import requests

#print(requests.__version__)

def generate_credentials():
    now = datetime.now()
    
    username = f"tesprogrammer{now.strftime('%d%m%y')}C19"
    password_plaintext = f"bisacoding-{now.day}-{now.month:02d}-{str(now.year)[-2:]}" 
    
    # Hash password menggunakan MD5
    password_md5 = hashlib.md5(password_plaintext.encode()).hexdigest()
    
    return username, password_md5, password_plaintext

# Generate username dan password
username, password_md5, password_plaintext = generate_credentials()

print("Username:", username)
print("Password (MD5):", password_md5)
print("Password Plaintext:", password_plaintext)

# URL API
api_url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

# Data untuk dikirim ke API
payload = {
    "username": username,
    "password": password_md5
}

# Kirim permintaan POST ke API
try:
    response = requests.post(api_url, data=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
    #print("Response Headers:", response.headers)
except Exception as e:
    print("Terjadi kesalahan saat mengakses API:", str(e))
