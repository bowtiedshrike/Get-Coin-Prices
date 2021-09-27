from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
coin_list = []

supported_coins = cg.get_coins_list()

filename = 'coinlist.csv'
with open(filename, 'w') as file_object:
    file_object.write('Symbol,Name\n')
    while True:
        resp= input("Please enter the coin name "
                    "(Type 'done' when finished):")
        if resp == 'done':
            break
        for coin in supported_coins:
            if resp == coin['id']:
                coin_id = resp
                coin_sym = coin['symbol']
                print(f"ID by name as {resp}. Symbol is {coin_sym}.")
            elif resp == coin['symbol']:
                coin_id = coin['id']
                coin_sym = resp
                print(f"ID by symbol as {resp}. Name is {coin_id}.")
        if not coin_id:
            print(f'{resp} is not a supported coin or symbol.')
        elif coin_id in coin_list:
            print(f"{resp} is already in the list")
        else:
            file_object.write(f'{coin_sym},{coin_id}\n')
            coin_list.append(coin_id)
        coin_id = 0
        coin_sym = 0
    print(f"Your chosen coins are:{coin_list}")   






