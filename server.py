from flask import Flask
import threading
from app import app as bot_app  # अगर तुम्हारा Telegram bot app.py में है

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running fine on Render!"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    bot_app.run()
