import hashlib
from datetime import datetime
import requests

print(requests.__version__)

# Fungsi untuk menghasilkan username dan password dinamis
def generate_credentials():
    # Ambil waktu sekarang berdasarkan waktu server
    now = datetime.now()
    
    # Format username
    username = f"tesprogrammer{now.strftime('%d%m%y')}C18"
    
    # Format password plaintext
    password_plaintext = f"bisacoding-{now.day}-{now.month}-{str(now.year)[-2:]}"
    
    # Hash password menggunakan MD5
    password_md5 = hashlib.md5(password_plaintext.encode()).hexdigest()
    
    return username, password_md5, password_plaintext

# Generate username dan password
username, password_md5, password_plaintext = generate_credentials()

# Cetak username dan password
#print("Username:", username)
#print("Password Plaintext:", password_plaintext)

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
except Exception as e:
    print("Terjadi kesalahan saat mengakses API:", str(e))
