from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

with open("C:\Projetos\Python\Selenium\\login_automation\config.json") as config:
    credential = json.load(config)


driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe")
tab = 1

# login Facebook
try:
    driver.get("https://pt-br.facebook.com/login/")
    driver.find_element_by_name("email").send_keys(credential['facebook']['un'])
    driver.find_element_by_name("pass").send_keys(credential['facebook']['pw'])
    driver.find_element_by_name("pass").send_keys(Keys.ENTER)
    print("Facebook Logged")
    time.sleep(1)
except:
    print("Failed to log on Facebook")

#login instagram
try:
    driver.execute_script('''window.open("https://www.instagram.com/accounts/login/?hl=pt-br","_blank");''')
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(1)
    driver.find_element_by_tag_name("button").click()
    time.sleep(1)
    print("Instagram Logged")
    tab += 1
except:
    print("Failed to log on instagram")

# #login whats
try:
    driver.execute_script('''window.open("https://web.whatsapp.com/","_blank");''')
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(1)
    print("WhatsApp Loaded")
    tab += 1
except:
    print("Failed to log on whats")

# #login github
try:
    driver.execute_script('''window.open("https://github.com/login","_blank");''')
    driver.switch_to.window(driver.window_handles[tab])
    driver.find_element_by_name("login").send_keys(credential['github']['un'])
    driver.find_element_by_name("password").send_keys(credential['github']['pw'])
    driver.find_element_by_name("commit").click()
    time.sleep(1)
    print("Github Logged")
    tab += 1
except:
    print("Failed to log on github")



#login discord
try:
    driver.execute_script('''window.open("https://discordapp.com/login","_blank");''')
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/input").send_keys(credential['discord']['un'])
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys(credential['discord']['pw'])
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/button[2]").click()
    time.sleep(1)
    print("Discord Logged")
    tab += 1
except:
    print("Failed to log na Discord")


try:
    driver.execute_script('''window.open("https://iqoption.com/en/login","_blank");''')
    driver.switch_to.window(driver.window_handles[tab])
    time.sleep(2)
    driver.find_element_by_name("email").send_keys(credential['iqOption']['un'])
    driver.find_element_by_name("password").send_keys(credential['iqOption']['pw'])
    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button[1]").click()
    time.sleep(1)
    print("IQOption Logged")
    tab += 1
except:
    print("Falha ao logar na iqOption")
#template
# try:
#     driver.execute_script('''window.open("login_url","_blank");''')
#     driver.switch_to.window(driver.window_handles[tab])
#     time.sleep(1)
#     driver.find_element_by_name("login").send_keys(credential['aplication']['un'])
#     driver.find_element_by_name("password").send_keys(credential['aplication']['pw'])
#     driver.find_element_by_name("commit").click()
#     time.sleep(1)
#     print("Aplication Logged")
#     tab += 1
# except:
#     print("Failed to log on Aplication")