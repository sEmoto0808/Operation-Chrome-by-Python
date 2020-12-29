import chromedriver_binary
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys('ChromeDriver')
time.sleep(3)
search_box.submit()

# Google検索結果のタイトルを取得してcsv形式で書き出す
with open('result_title.csv','w') as f:
    for g_h3 in driver.find_elements_by_css_selector(".g h3"):
        f.write('{0}\n'.format(g_h3.text))

driver.save_screenshot('初めてのWeb自動操作.png')
time.sleep(3)

target = driver.find_element_by_id("pnnext")
next_page = target.get_attribute("href")

# 次へボタンまでスクロールする
actions = ActionChains(driver)
actions.move_to_element(target)
actions.perform()
time.sleep(3)

# 次のページを表示する
driver.get(next_page)
with open('result_title2.csv','w') as f2:
    for g_h3 in driver.find_elements_by_css_selector(".g h3"):
        f2.write('{0}\n'.format(g_h3.text))
time.sleep(5)

# Chromeを閉じる
driver.quit()
