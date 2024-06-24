import requests
import pandas as pd
import yfinance as yf
import datetime

# AlgoTelegramBot klassi
class AlgoTelegramBot:
    def __init__(self, bot_token, chat_id):
        self.bot_token = bot_token
        self.chat_id = chat_id

    def send_telegram_signal(self, message):
        url = f'https://api.telegram.org/bot{self.bot_token}/sendMessage?chat_id={self.chat_id}&text={message}'
        response = requests.get(url)
        return response.status_code

# Stock ma'lumotlarini olish funktsiyasi
def get_stock_data(stock_symbol):
    stock = yf.Ticker(stock_symbol)
    stock_data = stock.history(period='1d')
    return stock_data

# Bot token va chat ID ni o'zgartiring
bot_token = '7053826131:AAF5mwMwG83s40MJpPUJCTqrYSCN96pSB08'
chat_id = '5043945231'

# AlgoTelegramBot obyektini yaratish
bot = AlgoTelegramBot(bot_token, chat_id)

# Kunda avtomatik signal yuborish uchun funktsiya
def send_daily_signals():
    # Stock simvolini o'zgartiring (masalan, 'AAPL' - Apple)
    stock_symbol = 'AAPL'
    stock_data = get_stock_data(stock_symbol)

    # Agar stock narxi kundalik balandlikka yetgan bo'lsa, "bayi" signalini yuborish
    if stock_data['Close'][-1] > stock_data['Close'].rolling(window=50).mean()[-1]:
        message = f"Bayi signal: {stock_symbol} - {stock_data['Close'][-1]}"
        bot.send_telegram_signal(message)
        print("Bayi signal yuborildi.")
    else:
        print("Signal yuborilmadi. Narx kundalik balandlikka yetmadi.")
# Kunda avtomatik signal yuborishni boshlash
send_daily_signals()