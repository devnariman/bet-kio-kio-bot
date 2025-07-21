from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import os



class Bet_Bot:
    def __init__(self, URL):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)  
        
    
    def login(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#btn-login-navbar-group")
        login_button.click()
        time.sleep(15)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "#input-login-email")
        email_input.send_keys("narimanpc1382@gmail.com")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "#input-login-password")
        password_input.send_keys("dev2256N")
        pres_login = self.driver.find_element(By.CSS_SELECTOR, "#btn-login")
        pres_login.click()
   



    def play_game(self):
        enfegar = self.driver.find_element(By.CSS_SELECTOR, "#game-link-button > div > div > img")
        enfegar.click()
        time.sleep(25)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "egamings_container gameIframe"))
            )
        except TimeoutException:
            self._save_page()
            return


        ok_btn = self.driver.find_element(By.CSS_SELECTOR, "#disconnected-btns > button")
        ok_btn.click()
        time.sleep(2)
        pres_history = self.driver.find_element(By.CSS_SELECTOR, "#history-tab")
        pres_history.click()
        time.sleep(2)        

    def get_number_of_bets(self):
        try:
            bet = self.driver.find_element(By.CSS_SELECTOR, "#history-wrapper > div:nth-child(2)")
            return bet.get_attribute("innerHTML")
        except Exception as e:
            print(f"Error getting number of bets: {e}")
            return 0


    def __del__(self):
        self.driver.quit()


class Coefficient:

    def __init__(self):
        self.list = []
        self.unit = []
        self.list_unitKasr_1 = []
        self.list_unitKasr_0 = []
    def mathican(self):
        number_of_zero = 0
        number_of_one = 0
        counter = 0
        for i in self.list:
            for j in i:
                if j == 0:
                    number_of_zero = number_of_zero + 1
   
                else:
                    number_of_one = number_of_one + 1
        
                counter = counter + 1
            
        
        print("counter : ",counter)
        print("all counter of Ones(1) : ", (number_of_one/counter) * 100)
        print("all counter of Zeros(0) : ", (number_of_zero/counter) * 100)

        last_unit = self.list[-1]  
        one_num = last_unit.count(1)
        zero_num = last_unit.count(0)
        total = one_num + zero_num
        print("------>")
        print("total this unit = ", total)
        percent_1 = (one_num / total) * 100
        percent_0 = (zero_num / total) * 100
        self.list_unitKasr_1.append(percent_1)
        self.list_unitKasr_0.append(percent_0)
        print("Analyzing new unit:")
        print("Ones (1):", one_num)
        print("Zeros (0):", zero_num)
        print("Percentage of ones:", percent_1)
        print("Percentage of zeros:", percent_0)
        try:
            print("Fractions so far (ones %):", self.list_unitKasr_1[-3:])
            print("Fractions so far (zeros %):", self.list_unitKasr_0[-3:])
        except:
            pass

    def insert_unit(self , unit):
        self.list.append(unit)
        os.system('cls')
        print("------------------------")
        print("New unit inserted:")
        print(self.list)
        self.mathican()
        print("------------------------")
        

    def insert_number(self , num):
        temp = 0
        if num < 2.00:
            temp = 0
        else:
            temp = 1
        self.unit.append(temp)
        print("New number inserted:", num)
        if len(self.unit) == 5:
            self.insert_unit(self.unit.copy())
            self.unit.clear()
        else:
            None


