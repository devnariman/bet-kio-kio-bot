from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.common.by import By
import time
class Bet_Bot:
    def __init__(self, URL):
        self.driver = webdriver.Chrome()
        self.driver.get(URL)  


    
    def login(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#btn-login-navbar-group")
        login_button.click()
        time.sleep(8)
        email_input = self.driver.find_element(By.CSS_SELECTOR, "#input-login-email")
        email_input.send_keys("narimanpc1382@gmail.com")
        password_input = self.driver.find_element(By.CSS_SELECTOR, "#input-login-password")
        password_input.send_keys("dev2256N")
        pres_login = self.driver.find_element(By.CSS_SELECTOR, "#btn-login")
        pres_login.click()
        time.sleep(8)



    def play_game(self):
        enfegar = self.driver.find_element(By.CSS_SELECTOR, "#game-link-button > div > div > img")
        enfegar.click()
        time.sleep(5)


        try:
            WebDriverWait(self.driver, 20).until(
                EC.frame_to_be_available_and_switch_to_it((By.ID, "egamings_container gameIframe"))
            )
        except TimeoutException:
            self._save_page()
            return

        time.sleep(20)
        
        ok_btn = self.driver.find_element(By.CSS_SELECTOR, "#disconnected-btns > button")
        ok_btn.click()
        time.sleep(1)
        pres_history = self.driver.find_element(By.CSS_SELECTOR, "#history-tab")
        pres_history.click()
        

    def get_number_of_bets(self):
        try:
            bet = self.driver.find_element(By.CSS_SELECTOR, "#history-wrapper > div:nth-child(2)")
            return bet.get_attribute("innerHTML")
        except Exception as e:
            print(f"Error getting number of bets: {e}")
            return 0


    def __del__(self):
        self.driver.quit()