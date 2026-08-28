import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
BALE_TOKEN = os.getenv("BALE_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
WP_API_URL = os.getenv("WP_API_URL")

def send_bale_message(text):
    url = f"https://tapi.bale.ai/bot{BALE_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHANNEL_ID, "text": text})

def check_daily_events():
    try:
        response = requests.get(WP_API_URL)
        if response.status_code == 200:
            events = response.json()
            if events.get('message'):
                send_bale_message(events['message'])
    except:
        pass

def send_report_reminder():
    text = "همکاران گرامی مؤسسه حسابداری امین، لطفاً گزارش کار امروز و ساعت ورود و خروج خود را در کانال ثبت کنید."
    send_bale_message(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "report":
            send_report_reminder()
        elif sys.argv[1] == "events":
            check_daily_events()
