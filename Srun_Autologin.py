from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

schoolWebURL = 'https://172.31.14.49/srun_portal_success?ac_id=1&theme=pro'   #请替换成自己的校园网登录网站

username = '1824272506'   #你的账号
password = 'Saya114514'    #你的密码
domain = '中国BB机'       #校园网运营商，请填入全称：中国移动/中国联通/中国电信

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")   #忽略那个烦得要死的证书错误验证

driver = webdriver.Chrome(options=chrome_options)
driver.get(schoolWebURL)
time.sleep(3)

#如果出现bug无法忽略证书验证或者是其他浏览器会采用下列补救方案，没问题直接跳过（这个是自动点击证书验证里的高级然后允许访问）
if driver.find_elements("id", "details-button"):         
    details_button = driver.find_element("id", "details-button")
    details_button.click()
    time.sleep(2)

if driver.find_elements("id", "proceed-link"):
    proceed_link = driver.find_element("id", "proceed-link")
    proceed_link.click()
    time.sleep(2)

if driver.find_elements("id", "login-account"):   #检测登录按键
    ele = driver.find_element("id", "login-account")
    if ele.is_enabled():
        print("当前状态：未登录，即将进行登录操作......")
        ele_username = driver.find_element("id", "username")   #输入账号密码并选择运营商
        ele_username.send_keys(username)
        ele_password = driver.find_element("id", "password")
        ele_password.send_keys(password)
        
        domain_element = driver.find_element("id", "domain")
        if domain_element:
            select = Select(domain_element)
            select.select_by_visible_text(domain)
            ele.click()
            time.sleep(3)
            print("当前状态：已登录")
        else:
            print("坏了，没找到你的运营商选择框在哪...")
elif driver.find_elements("id", "logout"):    #如果已经登录会跳转到这里找注销
    ele = driver.find_element("id", "logout")
    if ele.is_enabled():
        print("当前状态：已登录")
else:
    print("超时了...要不......再试试？")

driver.quit()
