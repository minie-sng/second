import time
from selenium import webdriver

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(url=URL)

print('아이돌 그룹(ex.트와이스, 엑소)')
group_list = input('>> ').split(',')

member_lists = []
for group in group_list:
    member_list = []
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(group)

    search_btn=driver.find_element_by_class_name("bt_search")
    search_btn.click()

    profile = driver.find_element_by_class_name("detail_profile")
    members = profile.find_element_by_xpath('//*[@id="people_info_z"]/div/div[2]/div[1]/div/dl/dd[2]')

    for member in members.find_elements_by_css_selector('a'):
        m = member.text
        print(m, end=' ')
        member_list.append(m)

    print('')
    member_lists.append(member_list)

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()