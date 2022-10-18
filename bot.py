import telebot
import requests
from time import time ,sleep

api_bot="5304508315:AAHoh1pIroprjqpGv7rL0jG-hidgbzeXVxM"
bot=telebot.TeleBot(api_bot , parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "به ربات اعلان قیمت تتر خوش اومدین")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "با  نوشتن /price میتوانید قیمت تتر را دریافت کنید.")


@bot.message_handler(commands=["price","PRICE"])

def send_price(message):
    bot.reply_to(message, "قیمت تتر به کانال ارسال شد.  \n https://t.me/+FpwNzc1PKm00NDg0 ")
    while True:
        huluex =(requests.get('https://api.huluex.com/api/market/getCoinsPrice')).json()
        nobitex=(requests.post('https://api.nobitex.ir/market/stats',data={"srcCurrency":"usdt","dstCurrency":"rls"})).json()
        wallex=(requests.get("https://api.wallex.ir/v1/markets")).json()
        btcprice=(requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT")).json()
        tetherland=(requests.get("https://api.tetherland.com/currencies")).json()
        abantether=(requests.get("https://abantether.com/management/all-coins/")).json()
        ramzinex=(requests.get("https://publicapi.ramzinex.com/exchange/api/v1.0/exchange/pairs/11")).json()
        date=(requests.get('https://api.kavenegar.com/v1/0/utils/getdate.json')).json()
        huluex_sell =float(huluex[1]["sellPrice"])
        huluex_buy = float(huluex[1]["buyPrice"])
        nobitex_sell=float(nobitex['stats']['usdt-rls']['bestSell'])/10
        nobitex_buy = float(nobitex['stats']['usdt-rls']['bestBuy'])/10
        wallex_buy=float(wallex["result"]["symbols"]["USDTTMN"]["stats"]["askPrice"])
        wallex_sell = float(wallex["result"]["symbols"]["USDTTMN"]["stats"]["bidPrice"])
        btcprice=(float(btcprice['lastPrice']))
        tetherland = float(tetherland["data"]["currencies"]["USDT"]["price"])
        abantether_buy=float(abantether[265]["priceBuy"])
        abantether_sell=float(abantether[265]["priceSell"])
        ramzinex_sell=float(ramzinex["data"]["sell"])/10
        ramzinex_buy=float(ramzinex["data"]["buy"])/10
        date=(date['entries']['datetime'])
        min_buy = min(huluex_buy,nobitex_buy, wallex_sell, tetherland, abantether_buy,ramzinex_buy)
        max_sell = max(huluex_sell  ,nobitex_sell, wallex_buy, tetherland, abantether_sell,ramzinex_sell)
        if abantether[265]["symbol"]=="USDT" :

            r1 = (" 💰 BTC                     %0.0f \n🟢 huluex          sell: %0.0f     buy: %0.0f \n🟢 nobitex        sell: %0.0f     buy: %0.0f \n🟢 wallex           sell: %0.0f     buy: %0.0f \n🟢 tetherland  sell : %0.0f    buy: %0.0f \n🟢 abantether sell: %0.0f     buy: %0.0f \n🟢 ramzinex     sell: %0.0f     buy: %0.0f \n🛑Lowest buying price %0.0f And the highest selling price %0.0f  \n There is a price difference  💲%0.0f💲  \n %s 📅" % (btcprice, huluex_sell,huluex_buy,nobitex_sell, nobitex_buy, wallex_buy, wallex_sell, tetherland,tetherland , abantether_sell, abantether_buy, ramzinex_sell, ramzinex_buy , min_buy,max_sell,(max_sell-min_buy), date))
            bot.send_message(chat_id="-1001604653336", text=r1)
        else:
            r1 = (
                        "❌❌Abantether token has expired, please inform the system administrator \n  💰 BTC                     %0.0f \n🟢 huluex          sell: %0.0f     buy: %0.0f \n🟢 nobitex        sell: %0.0f     buy: %0.0f \n🟢 wallex           sell: %0.0f     buy: %0.0f \n🟢 tetherland  sell : %0.0f    buy: %0.0f \n🟢 ramzinex     sell: %0.0f     buy: %0.0f \n🛑Lowest buying price %0.0f And the highest selling price %0.0f  \n There is a price difference  💲%0.0f💲  \n %s 📅" % (
                btcprice, huluex_sell, huluex_buy, nobitex_sell, nobitex_buy, wallex_buy, wallex_sell, tetherland,
                tetherland, ramzinex_sell, ramzinex_buy, min_buy, max_sell,
                (max_sell - min_buy), date))
            bot.send_message(chat_id="-1001604653336", text=r1)
        sleep(20)


bot.infinity_polling()



