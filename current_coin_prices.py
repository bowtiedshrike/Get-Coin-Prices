from pycoingecko import CoinGeckoAPI
import csv

cg = CoinGeckoAPI()

coins =[]
filename = 'coinlist.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        coin_symbol = row[0]
        coin_name = row[1]
        coin_info = cg.get_price(ids = coin_name, vs_currencies = 'usd')
        price = coin_info[coin_name]['usd']
        combined = f'{coin_symbol},{coin_name},{price}'
        coins.append(combined)
print(coins)
       
file2 = 'coinprice.csv'
with open(file2,'w') as f2:
    f2.write('Symbol,Name,Price\n')
    for coin in coins:
        f2.write(f'{coin}\n')
    







