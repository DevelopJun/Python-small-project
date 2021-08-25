import requests
import re # 이거 회화 들고올떄 정규식 complile ^ 이거 써야해서 난중에 추가함 
from bs4 import BeautifulSoup

def create_soup(url):
    headers ={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
    
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 흐림, 어제보다 00도 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 00 (최저/최고)
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text() # 최저온도
    max_temp = soup.find("span", attrs={"class":"max"}).get_text() # 최대온도 
    # 오전 오후 강수확률
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()
    # 미세먼지 정보
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()  # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text()  # 초미세먼지
    
    # 출력 
    print(cast)
    print("현재 {} (최저 {} / 최괴 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {} / 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("미세먼지 {}".format(pm25))
    print()

def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # 여기서 limit이 li 태그를 찾는데 3개까지 찾아라는거임.
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print(" (링크 : {})".format(link))
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3) # 여기서 limit이 li 태그를 찾는데 3개까지 찾아라는거임.
    for index, news in enumerate(news_list):
        a_indx = 0
        img = news.find("img")
        if img:
            a_indx = 1 # img 태그가 있으면 1번째 img 태그의 정보를 사용

        a_tag = news.find_all("a")[a_indx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print("{}. {}".format(index, title))
        print(" (링크 : {})".format(link))
    print()

# def scrape_english():
#     print("[오늘의 영어 회화]")
#     url ="https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english#;"
#     soup = create_soup(url)
#     sentences = soup.find_all("div", attrs={"id":re.compile"^conv_kor_t"})
#     print()

#     print()

if __name__ == "__main__":
    # scrape_weather()  # 오늘의 날씨정보 가져오기 
    scrape_headline_news() # 해드라인 뉴스 정보 가져오기
    # scrape_it_news() # IT 뉴스 정보 가져오기
    