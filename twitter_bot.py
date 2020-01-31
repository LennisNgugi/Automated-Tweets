from selenium import webdriver
from time import sleep

from secrets import username, password, status

class Twitter():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://twitter.com/')

        sleep(5)

        #Username is pulled from secrets.py file
        email_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div[1]/form/div/div[1]/div/label/div[2]/div/input')
        email_in.send_keys(username)

        #Username notification
        print('Username entered')
 
        #Wait 10 seconds to avoid the typing biomatics trigger 
        sleep(10)

        #Password is pulled from the secrets.py file
        pw_in = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div[1]/form/div/div[2]/div/label/div[2]/div/input')
        pw_in.send_keys(password)

        #Password notification
        print('Password entered')

        #Wait 10 seconds to avoid the typing biomatics trigger 
        sleep(10)

        #Login in button
        login_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div[1]/div[1]/div[1]/form/div/div[3]/div/div/span/span')
        login_btn.click()

        #Successful log
        print('Successful twitter log in')

        #wait 10 seconds 
        sleep(10)

        #Redirect to compose bar page
        self.driver.get('https://twitter.com/compose/tweet')

        #wait 5 seconds
        sleep (5)
        
        #Twitter Compose 
        print('Twitter composer / Tweet successfuly loaded')

        #Tweet something :D
        whatsHappening_in = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div/div/div/div[2]/div/div/div/div')
        whatsHappening_in.send_keys(status)

        #wait 10 seconds
        sleep(10)

        #Tweet Button
        login_btn = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[1]/div/div/div/div[2]/div[2]/div/div[3]/div/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        login_btn.click()

        #Tweet Successful
        print('Tweet Successful')


print('Twitter Script has started')

bot = Twitter()
bot.login()
