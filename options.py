from time import sleep

def authorize(browser):
    login_input = browser.find_element_by_id('quick_email')
    login_input.send_keys(input('Login: '))
    password_input = browser.find_element_by_id('quick_pass')
    password_input.send_keys(input('Password: '))
    login_button = browser.find_element_by_id('quick_login_button')
    login_button.click()
    sleep(5)
    check_code_input = browser.find_element_by_id('authcheck_code')
    check_code_input.send_keys(input('Code: '))
    check_code_submit = browser.find_element_by_id('login_authcheck_submit_btn')
    check_code_submit.click()
    while True:
        try:
            is_login = browser.find_element_by_class_name('TopNavBtn__profileName')
            print('Success login!')
            sleep(5)
            break
        except:
            print('Waiting login...')
            sleep(1)
    return 0