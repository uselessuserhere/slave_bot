from time import sleep
from sys import platform

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from options import authorize
from random import randint


opts = Options()
opts.add_argument("user-data-dir=Default")

def use_graph():
    is_graph = input('[Да] Графический интерфейс: ')
    if is_graph.lower() == 'да' or is_graph == '':
        opts.headless = False
    elif is_graph.lower() == 'нет':
        opts.headless = True
    else:
        use_graph()
use_graph()

if platform == "linux" or platform == "linux2":
    browser = Chrome('./chromedriver', options=opts)
elif platform == "win32":
    browser = Chrome('chromedriver.exe', options=opts)


browser.get('https://vk.com/app7794757?ref=catalog_recent#/')

try:
    login_button = browser.find_element_by_id('quick_login_button')
    authorize(browser)
except:
    print('Already authorized.')
    sleep(5)

def mode():
    print('Введите режим.')
    print('    [1] Фарм денег')
    print('    [0] Фарм рабов')
    isM = input('Режим: ')
    try:
        isM = bool(int(isM))
    except:
        print('Введите "1" или "0"')
        mode()
    return isM

isM = mode()

while True:
    try:
        user = str(randint(100000000,999999999))
        browser.get('https://vk.com/app7794757?ref=catalog_recent#/user/' + user)
        browser.get('https://vk.com/app7794757?ref=catalog_recent#/user/' + user)
        print('Попытка. Пользователь: ', user)
        sleep(randint(5,6))
        frames = browser.find_elements_by_tag_name('iframe')
        browser.switch_to.frame(frames[1])
        if isM:
            for i in range(randint(9, 18)):
                buy_button = browser.find_element_by_xpath('//*[@id="panel_user"]/div/div[4]/div/div/button')
                buy_button.click()
                sleep(randint(5, 6))
                sell_button = browser.find_element_by_xpath('//*[@id="panel_user"]/div/div[4]/div/div/button[2]')
                sell_button.click()
                sleep(randint(5, 6))
        buy_button = browser.find_element_by_xpath('//*[@id="panel_user"]/div/div[4]/div/div/button')
        buy_button.click()
        sleep(randint(4, 5))
        fetter_button = browser.find_element_by_xpath('//*[@id="panel_user"]/div/div[4]/div/div/button[1]')
        fetter_button.click()
        sleep(randint(3, 5))
        job_button = browser.find_element_by_xpath('//*[@id="panel_user"]/div/div[3]/div[2]/button')
        job_button.click()
        sleep(1)
        job_name = browser.find_element_by_xpath('//*[@id="modal_edit_user_job"]/div/div/form/div/div[1]/div/input')
        job_name.send_keys('(github)preposition17')
        submit_button = browser.find_element_by_xpath('//*[@id="modal_edit_user_job"]/div/div/form/div/div[2]/button')
        submit_button.click()
        sleep(randint(3, 5))
        print('Успешно. Пользователь: ', user)
    except KeyboardInterrupt:
        print('Выход.')
        exit()
    except:
        print('Ошибка. Пользователь:', user)
        continue