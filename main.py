import requests

# global variables
bot_token = '1715482567:AAFJ9hfFDzA8aHAoUueyX_7QSsXBgEKImUY'
chat_id = '445036648'


def get_prices():
    coins = ["BTC", "LUNA", "WAVES", "ZEC", "FTM", "ALGO", "XTZ", "CSPR", "BAT"]

    crypto_data = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD,BTC".format(",".join(coins))).json()[
        "RAW"]

    data = {}
    for i in crypto_data:
        data[i] = {
            "coin": i,
            "price": crypto_data[i]["USD"]["PRICE"],
            "priceBTC": crypto_data[i]["BTC"]["PRICE"]
            # "change_day": crypto_data[i]["USD"]["CHANGEPCT24HOUR"],
            # "change_hour": crypto_data[i]["USD"]["CHANGEPCTHOUR"]
        }

    return data


def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"
    # send the msg
    requests.get(url)


# # main fn
# def main():
#     send_message(chat_id=chat_id, msg=f'{get_prices}')

def main():
    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        priceBTC = crypto_data[i]["priceBTC"]
        send_message(chat_id=chat_id, msg=f'Coin: {coin}\n Price: ${price:,.2f}\n BTC: ₿ {priceBTC}\n\n')


# fancy way to activate the main() function
if __name__ == '__main__':
    main()
