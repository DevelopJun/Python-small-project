import requests
import re
import csv
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for i in range(1, 6):
    url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)
    print("페이지 :", i)
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})


    for item in items:
        # 광고 제품은 제외
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
        if ad_badge:
            # print("<광고 상품 제외 합니다.>")
            continue

        name = item.find("div", attrs={"class":"name"}).get_text()

        # 한컴 제품 제외 
        if "한성" in name:
            # print("<한성 상품 제외합니다.>")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
    
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회 
        rate = item.find("em", attrs={"class":"rating"}) # 평점
        if rate:
            rate = rate.get_text()
        else:
            # print("<평점 없는 상품 제외 합니다.>")
            continue

        rate_count = item.find("span", attrs={"class":"rating-total-count"}) # 평점수
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
            # print("리뷰수", rate_count)
        else:
            # print("<평점 수 없는 상품 제외 합니다.>")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 100:
            print(name, price, rate, rate_count)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_count}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) #줄 긋기 



    # 그러면 이제 파이썬 크롤링으로 -> 정보를 다 들고오고, 이거를 txt, csv 대부분 csv로 가지고 온 다음에, -> 데이터 분석을 판다스나, 텐서플로우로 적용하는 방식
