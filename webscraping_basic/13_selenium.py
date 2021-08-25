import time
from selenium import webdriver


browser = webdriver.Chrome() # 예를 들어서 지금 chrome(여기) 저 여기로 되어 있는 부분이 그 크롬 드라이브 경로인거임. 지금은 파이썬 워크스페이스에 내가 구글 
# 드라이브 exe 바로 나둬서 그냥 빈칸으로 둔거임. 

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력
browser.find_element_by_id("id").send_keys("naver_id") # 여기에 직접 아이디 비번 넣으면 로그인 된다. 
browser.find_element_by_id("pw").send_keys("password")

# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id 를 새로 입력 
# browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html 정보 출력
print(browser.page_source)


# 7. 브라우저 종료
# browser.close() # 현재 탭만 종료 
browser.quit() # 전체 브라우저 종료