from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭 
browser.find_element_by_link_text('가는날 선택').click()

# 이번달 27일, 27일 선택
# browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() #[0] -> 이번달

# browser.find_elements_by_link_text("27")[1].click() #[0] -> 다음달
# browser.find_elements_by_link_text("28")[1].click() #[0] -> 다음달
# 지금 [0] 이런거 왜 하는거냐면 글자로 링크 택스트 했는데 7월인지 8월인지 모르니까 저걸 나눠줘야하는거임 

# 이번달 27일, 다음달 28일 선택 
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() #[1] -> 다음달

# 제주도 선택 
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권 검색 클릭
browser.find_element_by_link_text('항공권 검색').click()

try:
    elem = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행 
    print(elem.text) # 첫번째 결과 출력 
finally:
    browser.quit()

# 10초 기다리는거임. 저 뒤에 xpath가 나올때 까지 


# # 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]").click()
# print(elem.text)

# 구글 무비 그 다음에 넘어가야함 