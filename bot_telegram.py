import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def kirim_laporan(pesan):
    url = "https://api.telegram.org/bot" + TOKEN + "/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": pesan,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.json()
    except Exception as e:
        return {"ok": False, "error": str(e)}

if __name__ == "__main__":
    hasil = kirim_laporan("Tes Bot Berhasil! Sistem Absensi Driver siap digunakan.")
    print(hasil)
