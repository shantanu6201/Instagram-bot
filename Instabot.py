from selenium import webdriver
#selenium module is used for web automation , webdriver is used for automation in Google Chrome
import time
from secrets import username
from secrets import password
#secrets.py file contains username and password of the user
class Instabot:
    def __init__(self ,username,password):
        self.driver = webdriver.Chrome("C://chromedriver")
        self.username = username
        #opens inatagram
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        #enters username
        self.driver.find_element_by_name("username").send_keys(username)
        time.sleep(2)
        #enters password
        self.driver.find_element_by_name("password").send_keys(password)
        time.sleep(2)
        #clicks login button
        self.driver.find_element_by_xpath("//div[text()='Log In']").click()
        time.sleep(4)
        # clicks Not Now upon logging in
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
        time.sleep(3)

    def getunfollowers(self):
    # clicks on username to open profile
        self.driver.find_element_by_class_name("gmFkV").click()
        time.sleep(3)
        # clicks followers
        self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
        followers = self._get_names()
        time.sleep(2)
        # opens following
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
        following = self._get_names()
        time.sleep(2)
        # compares followers and following lists
        not_following_back = [user for user in following if user not in followers]
        print(not_following_back)
        self.driver.find_element_by_css_selector("#react-root > section > main > div > header > section > div.nZSzR > div > button > svg").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Log Out')]").click()
        time.sleep(2)
        
    def _get_names(self):
        time.sleep(2)
        # path for scroll box
        scroll_box = self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div.isgrP")
        last_ht, ht = 0, 1
        # scrolls to the end of scroll box
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # path for close button
        self.driver.find_element_by_css_selector("body > div.RnEpo.Yx5HN > div > div:nth-child(1) > div > div:nth-child(3) > button > svg > path")\
            .click()
        time.sleep(2)
        return names
    

mybot = Instabot(username,password)
mybot.getunfollowers()
