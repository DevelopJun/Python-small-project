import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
} 
# 여기서 헤드 값을 쓰는 이유가 지금 접속경로가 한국어가 아니라 영어로 쓰는걸 아래에 html 불러오기로 확인할 수 있어서 우리가 한국에서 들어간다는 걸 user agent로 컴퓨터에 알려줘야함. 

res = requests.get(url, headers=headers)
res.raise_for_status
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)


'''
with open("movies.html", "w", encoding="utf8") as f:
    # f.write(res.text)
    f.write(soup.prettify()) # 지금 위의 코드로 하니깐 html 문서를 이쁘게 출력이 안되어서, soup 라이브러리의 pretty 함수를 이용하면 이쁘게 보여짐.
'''