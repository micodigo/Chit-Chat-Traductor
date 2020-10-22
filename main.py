from selenium import webdriver
import threading
import requests
import time
import sys
import os

class watsapp:
    def __init__(self):
        pass

    def load_driver(self):
        path = os.getcwd()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(executable_path=path+"\\chromedriver.exe",options=chromeOptions)
        return driver
    
    def load_driver2(self):
        path = os.getcwd()
        chromeOptions = webdriver.ChromeOptions()
        chromeOptions.add_argument('--headless')
        chromeOptions.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(executable_path=path+"\\chromedriver.exe",options=chromeOptions)
        return driver

    def getname(self):
        name = input("Enter Name:- ")
        return name

    def search_contact(self,driver,name):
        user=driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        user.click()

    def select_lang(self):
        language2 = input("Enter Language that you understand:- ")
        language1 = input("Enter Language that other understand:- ")
        print()
        return language1,language2
# /html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div[1]/div/div/span[1]
    def open_translator(self,drivern,language):
        lang=' '+language
        drivern.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input').send_keys(lang)
        time.sleep(3)
        drivern.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button').click()
    
    def type_message(self):
        time.sleep(10)
        message=input("You :- ")
        return message
    
    def translate(self,drivern,message,name='You (Translated)'):
        x=drivern.find_element_by_xpath('//*[@id="tw-source-text-ta"]')
        x.click()
        x.send_keys(message)
        time.sleep(2)
        tmessage=drivern.find_element_by_xpath('//*[@id="tw-target-text"]/span').text
        time.sleep(1)
        x.clear()
        print(name+" :- "+tmessage)
        return tmessage

    def send_message(self,driver,tmessage):
        # //*[@id="main"]/footer/div[1]/div[2]/div/div[2]
        x=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        x.click()
        # print(tmessage)
        x.send_keys(tmessage)

        driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button').click()


def last_message(chat,driver,driver3,name):
    i=2
    l_msg=0
    while True:
        while True:
            try:
                driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div['+str(i)+']')
                i+=1
            except:
                i-=1
                break
        if driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div['+str(i)+']/div/div/span[1]').get_attribute("aria-label")==(name+":"):
            if l_msg!=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div/div[1]/div/span[1]/span').text:
                l_msg=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div['+str(i)+']/div/div/div/div[1]/div/span[1]/span').text
                chat.translate(driver3,l_msg,"\n"+name)
    
            


def load_all(chat,driver,driver2,name):
    while True:
        message=chat.type_message()
        tmessage=chat.translate(driver2,message.lower())
        time.sleep(3)
        chat.send_message(driver,tmessage)
        if message.lower()=='byee':
            break


if __name__ == "__main__":
    chat=watsapp()
    driver = chat.load_driver()
    driver2 = chat.load_driver2()
    driver3 = chat.load_driver2()
    driver.get("https://web.whatsapp.com/")
    driver2.get("https://www.google.com/search?safe=active&sxsrf=ALeKk00BcpJq8cWU4337YK52_inGm-Lrpg%3A1594063984628&ei=cHwDX_nxJa7vz7sP8Niw0Ak&q=google+translator+&oq=google+translator+&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIHCAAQFBCHAjIICAAQsQMQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHUJWhA1iVoQNgr9sDaABwAngAgAGLAYgBiwGSAQMwLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwj56bWMr7nqAhWu93MBHXAsDJoQ4dUDCAw&uact=5")
    driver3.get("https://www.google.com/search?safe=active&sxsrf=ALeKk00BcpJq8cWU4337YK52_inGm-Lrpg%3A1594063984628&ei=cHwDX_nxJa7vz7sP8Niw0Ak&q=google+translator+&oq=google+translator+&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIHCAAQFBCHAjIICAAQsQMQgwEyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHUJWhA1iVoQNgr9sDaABwAngAgAGLAYgBiwGSAQMwLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwj56bWMr7nqAhWu93MBHXAsDJoQ4dUDCAw&uact=5")

    print("Please SCAN the watsapp QR Code")
    while True:
        temp=input("Have you scaned the QR Code ? (y/n)")
        if temp.upper()=='Y':
            break
        elif temp.upper()=='N':
            print("Please! Scan the QR code")
            continue
        else:
            print("--OOPS! Wrong input Please try again--")
            continue
    while True:
        try:
            name=chat.getname()
            chat.search_contact(driver,name)
            break
        except:
            print("Contact Not found")
            print("Try again")
    language1,language2=chat.select_lang()
    print("Please Wait.....")
    chat.open_translator(driver2,language1)
    chat.open_translator(driver3,language2)
    os.system('cls')
    t1=threading.Thread(target=load_all,args=(chat,driver,driver2,name))
    t2=threading.Thread(target=last_message,args=[chat,driver,driver3,name])
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    