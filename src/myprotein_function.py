import time
import re
from webdriver_wrapper import WebDriverWrapper
from selenium.webdriver.common.keys import Keys


def lambda_handler(*args, **kwargs):
    driver = WebDriverWrapper()

    driver.get_url('https://www.myprotein.com/nutrition/protein.list')

    # driver.set_input_value('//input[@name="q"]', '21 buttons')

    # button = driver.find("(//input[@name='btnK'])[2]")
    # button.send_keys(Keys.TAB)
    # driver.click('//input[@name="btnK"]')

    time.sleep(2)
    offers_html = driver.get_inner_html(
        "//*[@class='stripBanner']//*[@class='stripBanner_text']//p")

    print("--------------------------")

    print('Banner element:', offers_html)

    voucher_code_reg = re.search(r"CODE\:(.*)", offers_html)
    # print("Code (match):", voucher_code_reg)
    print("Code (regex):", voucher_code_reg.group(0))
    voucher_code = voucher_code_reg.group(1).strip()
    print("Code:", voucher_code)

    voucher_text_reg = re.search(r"(.*)\|", offers_html)
    print("Code desc (regex):", voucher_text_reg.group(0))
    voucher_desc = re.sub('<[^<]+?>', ' ', voucher_text_reg.group(1).strip())
    print("Code description:", voucher_desc)

    print("--------------------------")

    # first_google_result_title = driver.get_inner_html(
    #     '(//div[@class="rc"]//a)[1]')

    # print("--------------------------")
    # print(first_google_result_title)
    # print("--------------------------")

    driver.close()
