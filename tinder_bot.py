from selenium import webdriver
from time import sleep
import random

username, password = "", ""

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome('chromedriver.exe')

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        btns = self.driver.find_elements_by_tag_name('button')
        cookies = filter(lambda x: "I Accept" in x.get_attribute("innerHTML"), btns)
        for cookie in cookies:
            cookie.click()
            break
        
        sleep(2)

        login = filter(lambda x: "Log in" in x.get_attribute("innerHTML"), btns)
        for btn in login:
            print(btn.get_attribute('innerHTML'))
            self.driver.execute_script("arguments[0].click();", btn)
            break

        sleep(2)

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[2]/button')
        self.driver.execute_script("arguments[0].click();", fb_btn)

        sleep(2)

        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        self.driver.execute_script("arguments[0].click();", login_btn)

        self.driver.switch_to_window(base_window)

        sleep(6)

        popup_1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        self.driver.execute_script("arguments[0].click();", popup_1)

        sleep(6)

        popup_2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        self.driver.execute_script("arguments[0].click();", popup_2)

    def like(self):
        btns = self.driver.find_elements_by_tag_name('button')
        like = filter(lambda x: x.get_attribute("aria-label") == 'Like', btns)
        #like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button/span/svg/path')
        for like_btn in like:
            self.driver.execute_script("arguments[0].click();", like_btn)
            break

    def dislike(self):
        #dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        btns = self.driver.find_elements_by_tag_name('button')
        dislike = filter(lambda x: x.get_attribute("aria-label") == 'Nope', btns)
        for dislike_btn in dislike:
            self.driver.execute_script("arguments[0].click();", dislike_btn)
            break

    def check_for_tag(self):
        try:
            tag = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[7]/div/div[2]/div/div[2]')
            print(tag.get_attribute('innerHTML'))
            return True
        except:
            return False
        
    def check_for_verified(self):
        try:
            v = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div[1]/div[2]')
            return True
        except:
            return False

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.close_popup()
            except:
                num = random.randint(1, 10)
                if num > 3:
                    self.like()
                else:
                    self.dislike()
                    
                """
                print("Verified" if self.check_for_verified() else "Not verified")
                if self.check_for_tag() or self.check_for_verified():
                    self.like()
                else:
                    self.dislike()
                """
    
    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        self.driver.execute_script("arguments[0].click();", popup_3)

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        self.driver.execute_script("arguments[0].click();", match_popup)

bot = TinderBot()
bot.login()
sleep(4)
bot.auto_swipe()
