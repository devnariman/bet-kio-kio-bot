import time
from model import Bet_Bot , Coefficient
url = "https://kioki.com/en"
a = Bet_Bot(url)
time.sleep(6)
print("going to login !")
a.login()
time.sleep(5)
a.play_game()
time.sleep(3)
num = Coefficient()
parent_num = 0
on = True
while on:
    try:
        number = a.get_number_of_bets().replace("x", "")
        if number != parent_num:
            try:
                num.insert_number(float(number))
                parent_num = number
            except:
                print(f"Invalid number format: {number}")
                continue
        else:
            None
        
        time.sleep(0.3)  # Adjust the sleep time as needed
    except:
        pass



