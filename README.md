# Get-Coin-Prices
Choose crypto currencies available on CoinGecko and get the current prices


coin_name.py creates a list that current_coin_prices.py uses to pull coin prices with the CoinGecko API. Sample_tracker.xls is a sheet for tracking current value and prices.

### New to Python

If you are new to Python, you will need to first install Python 3 on your system (Search with duckduckgo or try https://www.python.org/downloads/ and pick the right one for your OS). If you have never used python before, there are many tutorials available on that site.

You will also need to install the requirements, which are listed in requirements.txt in this repository. You can install these with pip. See: https://packaging.python.org/tutorials/installing-packages/ for an overly-detailed walkthrough on installing packages (also note the commands are offered for both linux and windows; you may need to click the 'windows' tab to get the right code).

```pip install requirements.txt```

If you get an error message, try opening the requirements.txt and installing the packages without the version number. This is a simple program, so hopefully new versions of the packages will not break the script.


### Using the programs

There are three main files used here. Sample_tracker.xls is an example of the spreadsheet I use to track static and liquid balances. To update this workbook, I go to the TokenPrices sheet and I copy the 'price' to the 'last prices'. Then I paste the new current prices after I run current_coin_prices.py The spreadsheet updates with the new token prices. I update the liquidity pools as needed (yellow highlight) manually, and I yellow highlight any new liquidity/farming pools as needed. Please note that the numbers (including historical prices in the sheet) are all fake, and just given for examples. Also note that changing the coin order on TokenPrices will mess up your prices.

current_coin_prices.py will loop through the coin names (NOT symbols) listed in coinlist.csv and create a file called 'coinprice.csv'. It also provides a print output so that you can ensure it pulled the right coins. 

To generate coinlist.csv, please run 'coin_name.py'. This pulls the names directly from CoinGecko and avoids name errors. If coinlist.csv does not exist, you will get an error when you run current_coin_prices.py 

Please note that running coin_name.py will OVERWRITE the old coinlist.csv. Create a copy of coinlist.csv if you do not want to lose the information. The easiest way to update coinlist.csv is to copy/paste it (coinlist -Copy.csv), run coin_name.py with the new coins, open coinlist.csv, copy the new coin information and paste at the end of the old coins in coinlist -Copy.csv. Then delete coinlist.csv, and rename coinlist -Copy.csv to coinlist.csv.

coin_name.py will look for coins that match either the symbol or the name of the coin. Although the program will list all the matching coins, it only stores the last coin. For common coin symbols, use the name instead of the symbol. 
