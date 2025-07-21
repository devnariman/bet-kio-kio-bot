import time
from model import Bet_Bot
url = "https://kioki.com/en"
a = Bet_Bot(url)
time.sleep(5)
print("going to login !")
a.login()
a.play_game()
time.sleep(3)

parent_num = 0
on = True
while on:
    number = a.get_number_of_bets()
    if number != parent_num:
        print(f"New bet detected: {number.replace("x", "")}")
        # .
        # .
        # .ضریب ها اینجان 
        # .
        # .
        parent_num = number

    else:
        None
    
    time.sleep(0.5)  # Adjust the sleep time as needed
