import requests
res = requests.get("http://google.com")
res.raise_for_status()
# 그래서 항상 쌍으로 쓴다. 습관적으로 하면 될 듯? 

# res = requests.get("http://nadocoding.tistory.com")
print("응답코드 :", res.status_code) #200 이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")


print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)