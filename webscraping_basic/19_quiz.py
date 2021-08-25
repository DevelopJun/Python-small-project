import requests
import re
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# 여기서 soup 파일로 보고 html안에 우리가 원하는 정보가 있으면 그냥 하면되고, 안되면 user-agent를 사용하던지, 
# 아니면 셀레니움을 사용하던지 결정하면 된다. 
'''
with open("quiz.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
'''
# 지금 위에서 html 보니까 따로 셀레니움을 쓴다던지 유저 에이전트 쓸 필요가 없을듯? 이렇게 생각해야함.


propers = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")

for index, proper in enumerate(propers):
    deal = proper.find("td", attrs={"class":"col1"}).get_text()
    space = proper.find("td", attrs={"class":"col2"}).get_text()
    price = proper.find("td", attrs={"class":"col3"}).get_text()
    dong = proper.find("td", attrs={"class":"col4"}).get_text()
    floor = proper.find("td", attrs={"class":"col5"}).get_text()

    print("====== 매물{} ======".format(index+1))
    print(f"거래 : {deal}")
    print(f"면적 : {space} (공급/전용)")
    print(f"가격 : {price} (만원)")
    print(f"동 : {dong}")
    print(f"층 : {floor}")
 

'''
# 위에는 내가 짠 부분인데 사부님께서는 
data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr") # 점점 좁히는 방법임. 
for index, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("========== 매물 {} ===========".format(index+1))
    print("거래 :", columns[0].get_text().strip()) #strip은 간격 줄여주는 함수임 
    print("면적 :", columns[1].get_text().strip(), "(공급/전용)")
    print("가격 :", columns[2].get_text().strip(), "(만원)")
    print("동 :", columns[3].get_text().strip())
    print("층 :", columns[4].get_text().strip())
'''
