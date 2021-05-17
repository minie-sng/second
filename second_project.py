import time
from selenium import webdriver
import matplotlib
import matplotlib.pyplot as plt

URL = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)
driver.get(url=URL)

print('아이돌 그룹(ex.트와이스, 엑소)')
group_list = input('>> ').split(',')

member_lists = []
name_list = []
for group in group_list:
    member_list = []
    search_box=driver.find_element_by_name("query")
    search_box.send_keys(group)

    search_btn=driver.find_element_by_class_name("bt_search")
    search_btn.click()

    profile = driver.find_element_by_class_name("detail_profile")
    group_name = profile.find_element_by_xpath('//*[@id="people_info_z"]/div/div[2]/div[1]/div/dl/dd[1]/a/strong').text
    members = profile.find_element_by_xpath('//*[@id="people_info_z"]/div/div[2]/div[1]/div/dl/dd[2]')

    print(group_name, '-', end=' ')

    for member in members.find_elements_by_css_selector('a'):
        m = member.text
        print(m, end=' ')
        member_list.append(m)

    print('')
    member_lists.append(member_list)
    name_list.append(group_name)

    time.sleep(3)
    search_box = driver.find_element_by_name("query")
    search_box.clear()

print('\n')
print(name_list)

count_list = []
cyc_list = []
cyc = 0
for i in member_lists:
    count = 0
    for m in i:
        count += 1
    cyc += 1
    count_list.append(count)
    cyc_list.append(cyc)

print(count_list)

time.sleep(3)

driver.close()

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

color_list = {'lightpink','violet','thistle','mediumpurple','lavender','lightskyblue','lightblue','paleturquoise','mediumturquoise','aquamarine','mediumseagreen','lightgreen','palegreen','yellowgreen','khaki','burlywood','bisque','peachpuff','mistyrose','lightgray','rosybrown','lightcoral'}
color_list = list(color_list)

plt.figure(figsize=(8,8))
plt.bar(cyc_list, count_list, color=color_list[0])
plt.xticks(cyc_list, name_list, rotation='vertical', fontsize=8)
plt.suptitle('멤버 수', fontsize=15)
plt.ylabel('(단위 : 명)', fontsize=9)

plt.show()