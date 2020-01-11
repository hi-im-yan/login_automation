from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

with open("C:\Projetos\Python\Selenium\\login_automation\config.json") as config:
    credential = json.load(config)


driver = webdriver.Chrome(executable_path=r"C:\WebDriver\chromedriver.exe")
tab = 1

# login Facebook & load next app
try:
    driver.get("https://pt-br.facebook.com/login/")
    driver.execute_script('''window.open("https://www.instagram.com/accounts/login/?hl=pt-br","_blank");''') 
    driver.find_element_by_name("email").send_keys(credential['facebook']['un'])
    driver.find_element_by_name("pass").send_keys(credential['facebook']['pw'])
    driver.find_element_by_name("pass").send_keys(Keys.ENTER)
    print("Facebook Logged")
except:
    print("Failed to log on Facebook")

#login instagram & load next app
try:
    driver.switch_to.window(driver.window_handles[tab])
    driver.execute_script('''window.open("https://web.whatsapp.com/","_blank");''')
    driver.find_element_by_tag_name("button").click()
    print("Instagram Logged")
    tab += 1
except:
    print("Failed to log on instagram")

# #login whats & load next app
try:
    driver.switch_to.window(driver.window_handles[tab])
    driver.execute_script('''window.open("https://github.com/login","_blank");''')
    print("WhatsApp Loaded")
    tab += 1
except:
    print("Failed to log on whats")

# #login github & load next app
try:
    driver.switch_to.window(driver.window_handles[tab])
    driver.execute_script('''window.open("https://discordapp.com/login","_blank");''')
    driver.find_element_by_name("login").send_keys(credential['github']['un'])
    driver.find_element_by_name("password").send_keys(credential['github']['pw'])
    driver.find_element_by_name("commit").click()
    print("Github Logged")
    tab += 1
except:
    print("Failed to log on github")

#login discord & load next app
try:
    driver.switch_to.window(driver.window_handles[tab])
    driver.execute_script('''window.open("https://iqoption.com/en/login","_blank");''')
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[1]/div/input").send_keys(credential['discord']['un'])
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/div[2]/div/input").send_keys(credential['discord']['pw'])
    driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/form/div/div/div[1]/div[3]/button[2]").click()
    print("Discord Logged")
    tab += 1
except:
    print("Failed to log na Discord")

#login IQOption & load next app
try:
    driver.switch_to.window(driver.window_handles[tab])
    driver.find_element_by_name("email").send_keys(credential['iqOption']['un'])
    driver.find_element_by_name("password").send_keys(credential['iqOption']['pw'])
    driver.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/form/button[1]").click()
    print("IQOption Logged")
    tab += 1
except:
    print("Falha ao logar na iqOption")

#template
# try:
#     driver.switch_to.window(driver.window_handles[tab])
#     driver.execute_script('''window.open("login_url","_blank");''')
#     time.sleep(1)
#     driver.find_element_by_name("login").send_keys(credential['aplication']['un'])
#     driver.find_element_by_name("password").send_keys(credential['aplication']['pw'])
#     driver.find_element_by_name("commit").click()
#     time.sleep(1)
#     print("Aplication Logged")
#     tab += 1
# except:
#     print("Failed to log on Aplication")

# A ideia de abrir a próxima aba logo que abre a atual é para que enquanto faz o carregamento da próxima aba,
# a aba anterior esteja sendo preenchida com os dados de login.
# Desse modo quando for fazer o login na proxima aba não será preciso esperar o carregamento do formulário de login,
# pois já estará carregado. Isso evita o uso de time.sleep() e segundos adicionais na execução.