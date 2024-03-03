from forex_python.bitcoin import BtcConverter
from datetime import datetime

year = int(input("შეიყვანე ბიტკოინის შეძენის წელი: "))
month = int(input("შეიყვანე ბიტკოინის შეძენის თვე: "))
day = int(input("შეიყვანე ბიტკოინის შეძენის დღე: "))
cost = float(input("შეიყვანეთ თანხა, რაც გადაიხადეთ ბიტკოინის შეძენაში, ვალუტა - USD : "))

btc_converter = BtcConverter()
purchase_price = btc_converter.get_previous_price('USD', datetime(year, month, day))

if purchase_price is not None:

    current_bitcoin_rate = btc_converter.get_latest_price('USD')
    purchase_value = cost / purchase_price
    current_value = purchase_value * current_bitcoin_rate
    profit_loss = current_value - cost
    if profit_loss >= 0:
        print(f"თქვენ გაქვთ მოგება ${profit_loss:.2f} ბიტკოინის შეძენის შემდეგ.")
    else:
        print(f"თქვენ გაქვთ წაგება ${-profit_loss:.2f} ბიტკოინის შეძენის შემდეგ.")
else:
    print(" მონაცემები არ არის ხელმისაწვდომი მითითებულ თარიღზე.")

