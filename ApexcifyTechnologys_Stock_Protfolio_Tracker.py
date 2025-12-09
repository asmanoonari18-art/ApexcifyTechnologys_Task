# ------------------------------------------------------
#  STOCK PROTFOLIO TRACKER
# ------------------------------------------------------

import csv 
from datetime import datetime

# ANSI colors for good look
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
blue = '\033[94m'
cyan = '\033[96m'
magenta = '\033[95m'
bold = '\033[1m'
reset = '\033[0m'

# Stock Prices
prices = {
    'AAPL':185,
    'TSLA':250,
    'AMZN':165,
    'GOOGL':142,
    'MSFT':315,
    'NFLX':485,
}
portfolio = []

print(f'\n{cyan}{bold}🚀Stock Portfolio Tracker{reset}\n')
while True:
    stock = input(f'{yellow}📌 Enter stock symbol: {reset}').upper()
    if stock not in prices:
        print(f'{red}❌Stock not found! Avaiable: {list(prices.keys())}{reset}')
        continue

    qty = int(input(f'🔢Enter quantity of {stock}:'))
    buy_price = float(input(f'💰Enter buying price for {stock}L'))

    portfolio.append({
        'Stock':stock,
        'Quantity':qty,
        'Buy Price':buy_price,
        'Current Price':prices[stock]
    })

    choice = input('➕Add another stock (y/n): ').lower()
    if choice != 'y':
        break

#------- calculations-------
print(f'\n{magenta}{bold} 📊Calculating Portfolio...{reset}\n')
print(f'{blue}{bold}----------Portfolio Summary-------------{reset}\n')

'''
total_invest = total amount the user invested (sum of quantity * buy price).
total_current = total current market value (quantity * current price).
total_profit = total profit or loss (current value - investment).
'''

total_invest = 0
total_current = 0
total_profit = 0

for item in portfolio:
    investment = item['Quantity']*item['Buy Price']
    current_value = item['Quantity']*item['Current Price']
    profit_loss = current_value * investment

    total_invest += investment
    total_current += current_value
    total_profit += profit_loss

    color = green if profit_loss >= 0 else red
    emoji = '📈' if profit_loss >= 0 else '📉'

    print (f'{emoji}{bold}{item['Stock']}{reset} |'
           f'Qty: {item['Quantity']} |'
           f'Buy: ${item['Buy Price']} |'
           f'Curr: ${item['Current Price']} |'
           f'{color} PL: ${profit_loss: 2f}{reset}')
    print('\n'+'-'*40)

    color_t = green if total_profit >= 0 else red
    emoji_t = '💹' if total_profit >= 0 else '⚠️'

    print(f' 💵Total Investment: {yellow}${total_invest: 2f}{reset}')
    print(f'💼Current Value: {cyan}${total_current: 2f}{reset}')
    print(f'{emoji_t} Total Profit/Loss: {color_t}${total_profit: 2f}{reset}')
    print('-'*40+'\n')

    #------- Save Report------------
    save = input('💾Save report (txt/txt/no)?').lower()
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    if save == 'txt':
        filename = f'portfolio_{timestamp}.txt'
        with open(filename, 'w') as f:
            f.write('Stock Portfolio Report\n\n')
            for item in portfolio:
                investment = item['Quantity']*item['Buy Price']
                current_value = item['Quantity']*item['Current Price']
                profit_loss = current_value * investment

                f.write(f'{item['Stock']} | Qty {item['Quantity']} | Buy {item['Buy Price']} |'
                        f'Current {item['Current Price']} | PL {profit_loss: .2f}\n')
                
                f.write(f'\nTotal Investment: ${total_invest: .2f}\n')
                f.write(f'Current Values: ${total_current: .2f}\n')
                f.write(f'Profit/Loss: ${total_profit:.2f}\n')

        print(f'{green} ✔Saved as {filename}{reset}')

    elif save == 'csv':
        filename = f"portfolio_{timestamp}.csv"
        with open(filename, "w", newline="") as f:
          writer = csv.writer(f)
          writer.writerow(["Stock", "Quantity", "Buy Price", "Current Price", "Profit/Loss"])

          for item in portfolio:
             investment = item["Quantity"] * item["Buy Price"]
             current_value = item["Quantity"] * item["Current Price"]
             profit_loss = current_value - investment
             writer.writerow([item["Stock"], item["Quantity"], item["Buy Price"],
                             item["Current Price"], profit_loss])

        print(f"{green}✔ Saved as {filename}{reset}")

    else:
        print(f"{yellow}ℹ️ Report not saved.{reset}")

    print(f"\n{green}{bold}✨ Program Finished!{reset}")

